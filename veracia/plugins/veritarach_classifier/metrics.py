from veracia.core.plugin import EvalResult, MetricPlugin

_PREVIEW_LEN = 100


class VeritarachClassifierPlugin(MetricPlugin):
    def score(self, case: dict, actual: dict) -> EvalResult:
        text = case["input"]
        preview = text[:_PREVIEW_LEN] + ("..." if len(text) > _PREVIEW_LEN else "")

        return EvalResult(
            input=preview,
            expected=case["label"],
            actual=actual["label"],
            confidence=actual["confidence"],
            metadata={"correct": case["label"] == actual["label"]},
        )

    def aggregate(self, results: list[EvalResult]) -> dict:
        tp = sum(1 for r in results if r.expected == "ai_generated" and r.actual == "ai_generated")
        fp = sum(1 for r in results if r.expected == "human_written" and r.actual == "ai_generated")
        tn = sum(1 for r in results if r.expected == "human_written" and r.actual == "human_written")
        fn = sum(1 for r in results if r.expected == "ai_generated" and r.actual == "human_written")

        precision = tp / (tp + fp) if (tp + fp) else 0.0
        recall = tp / (tp + fn) if (tp + fn) else 0.0
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) else 0.0

        return {
            "confusion_matrix": {"tp": tp, "fp": fp, "tn": tn, "fn": fn},
            "precision": precision,
            "recall": recall,
            "f1": f1,
            "false_positive_rate": fp / (fp + tn) if (fp + tn) else 0.0,
        }
