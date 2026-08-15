from veracia.core.plugin import EvalResult, MetricPlugin

# matches HALLUCINATION_THRESHOLD in Hecate's pipeline/rag/evaluation.py
HALLUCINATION_THRESHOLD = 0.5


class HecateRAGPlugin(MetricPlugin):
    def score(self, case: dict, actual: dict) -> EvalResult:
        return EvalResult(
            input=case["question"],
            expected=case.get("expected_answer"),
            actual=actual["answer"],
            confidence=actual.get("faithfulness"),
            metadata={
                "faithfulness": actual.get("faithfulness"),
                "relevance": actual.get("relevance"),
            },
        )

    def aggregate(self, results: list[EvalResult]) -> dict:
        faithfulness_scores = [
            r.metadata["faithfulness"] for r in results if r.metadata.get("faithfulness") is not None
        ]
        relevance_scores = [
            r.metadata["relevance"] for r in results if r.metadata.get("relevance") is not None
        ]
        hallucinations = [r for r in results if r.metadata.get("faithfulness") is not None]
        hallucinated = [r for r in hallucinations if r.metadata["faithfulness"] < HALLUCINATION_THRESHOLD]

        return {
            "avg_faithfulness": (
                sum(faithfulness_scores) / len(faithfulness_scores) if faithfulness_scores else None
            ),
            "avg_relevance": (
                sum(relevance_scores) / len(relevance_scores) if relevance_scores else None
            ),
            "pct_hallucination": (
                len(hallucinated) / len(hallucinations) if hallucinations else None
            ),
        }
