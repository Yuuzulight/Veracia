from veracia.core.plugin import EvalResult
from veracia.plugins.veritarach_classifier.metrics import VeritarachClassifierPlugin


class VeritarachAdversarialPlugin(VeritarachClassifierPlugin):
    """Scores paraphrased versions of samples Veritarach already classified
    correctly. Every case is expected to carry an original_confidence field
    from before perturbation -- pre_accuracy is 1.0 by construction, since
    the dataset only contains samples that started out correct.
    """

    def score(self, case: dict, actual: dict) -> EvalResult:
        result = super().score(case, actual)
        result.metadata["original_confidence"] = case["original_confidence"]
        result.metadata["confidence_delta"] = actual["confidence"] - case["original_confidence"]
        return result

    def aggregate(self, results: list[EvalResult]) -> dict:
        summary = super().aggregate(results)
        matrix = summary["confusion_matrix"]
        total = sum(matrix.values())

        deltas = [r.metadata["confidence_delta"] for r in results]

        summary["pre_accuracy"] = 1.0 if results else None
        summary["post_accuracy"] = (matrix["tp"] + matrix["tn"]) / total if total else None
        summary["avg_confidence_delta"] = sum(deltas) / len(deltas) if deltas else None
        return summary
