# Architecture

## The interface everything else builds on

Two things: a plugin base class and a result type. Everything in `core/` is written against these and nothing else.

```python
@dataclass
class EvalResult:
    input: Any
    expected: Any
    actual: Any
    confidence: float | None
    metadata: dict  # whatever the plugin wants to carry through to the report

class MetricPlugin(ABC):
    @abstractmethod
    def score(self, case: dict, actual: Any) -> EvalResult: ...

    @abstractmethod
    def aggregate(self, results: list[EvalResult]) -> dict: ...
```

`score()` judges one prediction. `aggregate()` turns a full run into summary stats — an F1 number, a confusion matrix, an average faithfulness score, whatever the project needs. The runner and report generator only ever call these two methods; neither knows what "correct" means for RAG versus classification, and neither needs to.

## Runner

```python
class Runner:
    def __init__(self, predict_fn: Callable[[Any], Any], metric_plugin: MetricPlugin): ...
    def run(self, dataset: list[dict]) -> list[EvalResult]: ...
```

`run()` walks the dataset in order, calls `predict_fn(case["input"])`, and passes the case plus the prediction to `plugin.score()`. If `predict_fn` raises on a case, that case is recorded as a failure (input/expected preserved, `actual=None`, the exception message in `metadata["error"]`) and the run continues — one bad case in a 150-row dataset shouldn't kill the other 149.

## Dataset loading

`core/dataset.py` loads `.jsonl`, one case per line, and checks every row against a list of required fields before returning anything. A row missing a field is a hard error, not a skip — a dataset silently dropping rows would quietly shrink what's actually being tested, with no signal that it happened. Better to fail the load than ship an eval that's covering less than it claims to.

## Report

`core/report.py` takes the `list[EvalResult]` plus whatever `aggregate()` returned and writes a markdown file: a summary table, the worst N cases by confidence gap or misclassification, then the full result table. It doesn't know what the summary dict's keys mean — it just renders whatever's there.

## Plugin notes

**Hecate.** `HecateRAGPlugin` doesn't call RAGAS or touch Postgres itself — that stays entirely inside Hecate's own `pipeline/rag/evaluation.py`. The plugin's `score()` takes the two numbers Hecate's evaluator already produces (faithfulness, relevance) as part of `actual`, and reports them as-is rather than collapsing them into one score. This keeps Veracia's test suite free of a live database or judge-provider API key — the plugin is tested against fixture dicts, and wiring it to a real Hecate run is a separate integration step, not something `pytest` needs to do.

**Veritarach.** `VeritarachClassifierPlugin`'s `predict_fn` is an HTTP call to Veritarach's deployed `/predict` endpoint (`{"text": ...}` in, `{"label": "ai_generated" | "human_written", "confidence": float}` out). The confusion-matrix plugin only needs that. The generalization and adversarial plugins share the same scoring logic but run against different datasets — cross-model samples for one, paraphrased samples for the other — so the interesting part of those two is the dataset, not the plugin code.
