# Veracia

A small evaluation harness for two very different systems that turn out to ask the same question: is this model's output actually trustworthy, or does it just look fine at a glance?

[Hecate](https://github.com/Yuuzulight/Hecate) runs RAG over a document set and has to answer "is this response grounded in what we retrieved." [Veritarach](https://github.com/Yuuzulight/Veritarach) is a fine-tuned classifier that has to answer "is this text AI-generated." Different problems, different metrics, but both projects eventually need the same three things: run a labeled test set through a prediction function, score each case, and produce a report that says more than a single number.

Veracia is that shared piece. One runner, one report format, and a metric plugin per project. It doesn't train models and it doesn't host anything — you point it at a prediction function and a dataset, and it tells you what happened.

## Why this exists

Hecate's own eval code (`pipeline/rag/evaluation.py`) already computes faithfulness and relevance scores per answer. Veritarach reports a single F1 number and nothing else. Neither of those on their own tells you much about failure modes — a RAG pipeline can be faithful but useless, and a 99% F1 classifier can still be badly miscalibrated on the exact cases that matter most (false positives, in Veritarach's case, since flagging real human writing as AI-generated is the costlier mistake for a detector making public claims).

Building the scoring and reporting logic twice, once per project, means every fix has to happen twice too. Veracia exists so it only has to happen once.

## How it's put together

```
veracia/
├── core/                     # runner, report, dataset loader, plugin interface
└── plugins/
    ├── hecate_rag/           # wraps Hecate's faithfulness + relevance scores
    └── veritarach_classifier/  # confusion matrix, generalization, adversarial checks
```

The runner (`core/runner.py`) doesn't know anything about RAG or classification. It takes a `predict_fn`, a dataset, and a plugin, and for every case it calls `predict_fn(case["input"])` then hands the result to `plugin.score()`. All the project-specific logic — what counts as correct, what the summary stats look like — lives in the plugin. `core/report.py` turns the scored results into a markdown report without caring which plugin produced them.

```python
from veracia.core.runner import Runner
from veracia.core.dataset import load_dataset
from veracia.core.report import render_markdown
from veracia.plugins.veritarach_classifier.client import predict
from veracia.plugins.veritarach_classifier.metrics import VeritarachClassifierPlugin

dataset = load_dataset("datasets/veritarach_holdout_test.jsonl", required_fields=["input", "label"])
plugin = VeritarachClassifierPlugin()
runner = Runner(predict_fn=predict, metric_plugin=plugin)
results = runner.run(dataset)

render_markdown(results, plugin.aggregate(results), name="Veritarach holdout", path="reports/veritarach_holdout.md")
```

## The two plugins

**Hecate** wraps the two metrics Hecate's own evaluator already produces — faithfulness and relevance — and reports them separately rather than averaging them into one number. That's deliberate, not an oversight: Hecate's own docstring argues a composite score would hide the one distinction worth keeping (a faithful-but-irrelevant answer and an unfaithful one fail for completely different reasons). Veracia's eval set (`datasets/hecate_eval_qa.jsonl`) seeds from the same 12 questions Hecate's own test suite uses, so the two aren't scoring against different ground truth by accident.

**Veritarach** does three things:
- A real confusion matrix against a held-out set, broken out by TP/FP/TN/FN, with false positive rate called out on its own since that's the failure mode that actually matters for a public detector.
- A cross-model generalization check — new samples from a model that had no part in Veritarach's training mix (Claude, GPT-4o, and Gemini, per its training pipeline), to see whether accuracy holds up on writing style the model has never seen before.
- An adversarial pass — light paraphrasing of already-correctly-classified samples, to see how much confidence degrades under realistic evasion rather than synthetic noise.

Veritarach's own repo doesn't ship a held-out dataset (the training data is gitignored and lives only on the box it was trained on), so the holdout set here is Veracia's own, built independently rather than reused. If anything that's a stronger check — it means the 99.65% F1 Veritarach reports gets verified against data it never bootstrapped its own number from.

## What it found

All three Veritarach checks are run for real against the live deployment, not just fixtures — see [docs/examples](docs/examples). Short version: the 99.65% F1 figure doesn't hold up independently. Real F1 against Veracia's holdout is 0.62, and confidence sits within a ~0.2-wide band of the decision boundary across effectively every case tested, including ones that aren't ambiguous at all. Accuracy against a model outside the training mix drops to 8%. Full writeup, numbers, and what's actually happening (rather than just "it went down") are in the linked reports.

## Running it

```bash
pip install -e ".[dev]"
pytest
```

Reports land in `reports/` and aren't checked in — they're regenerated from whatever dataset and prediction function you point the runner at. `scripts/` has the generation scripts used to build the checked-in example reports and datasets.

## Status

Core interface and both plugins are built: runner, report generator, dataset loader, the Hecate RAG plugin, and Veritarach's confusion matrix, generalization, and adversarial checks. See the [issue tracker](https://github.com/Yuuzulight/Veracia/issues) for history. Still open: a live Hecate report (needs an actual Hecate deployment to run against), and whatever comes out of following up on the generalization gap above.
