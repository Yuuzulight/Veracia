from veracia.core.plugin import EvalResult
from veracia.plugins.veritarach_classifier.metrics import VeritarachClassifierPlugin


class VeritarachGeneralizationPlugin(VeritarachClassifierPlugin):
    """Same scoring as VeritarachClassifierPlugin, run against a model that
    had no part in Veritarach's training mix. aggregate() adds an accuracy
    delta against the in-distribution holdout accuracy, since the interesting
    question here isn't the raw number, it's how far it moved.
    """

    def __init__(self, baseline_accuracy: float | None = None):
        self.baseline_accuracy = baseline_accuracy

    def aggregate(self, results: list[EvalResult]) -> dict:
        summary = super().aggregate(results)
        matrix = summary["confusion_matrix"]
        total = sum(matrix.values())
        accuracy = (matrix["tp"] + matrix["tn"]) / total if total else None

        summary["accuracy"] = accuracy
        summary["baseline_accuracy"] = self.baseline_accuracy
        summary["accuracy_delta"] = (
            accuracy - self.baseline_accuracy
            if accuracy is not None and self.baseline_accuracy is not None
            else None
        )
        return summary
