from veracia.core.plugin import EvalResult
from veracia.plugins.veritarach_classifier.generalization import VeritarachGeneralizationPlugin


def _result(expected, actual):
    return EvalResult(input="...", expected=expected, actual=actual, confidence=0.8, metadata={})


def test_generalization_plugin_flags_out_of_distribution_samples():
    # 3 correct, 1 wrong on a cross-model set that's entirely ai_generated --
    # any human_written prediction here is the model failing to generalize.
    plugin = VeritarachGeneralizationPlugin(baseline_accuracy=0.95)
    results = [
        _result("ai_generated", "ai_generated"),
        _result("ai_generated", "ai_generated"),
        _result("ai_generated", "ai_generated"),
        _result("ai_generated", "human_written"),
    ]

    summary = plugin.aggregate(results)

    assert summary["accuracy"] == 0.75
    assert summary["baseline_accuracy"] == 0.95
    assert summary["accuracy_delta"] == 0.75 - 0.95


def test_reuses_the_confusion_matrix_from_the_base_plugin():
    plugin = VeritarachGeneralizationPlugin(baseline_accuracy=0.9)
    results = [_result("ai_generated", "ai_generated"), _result("ai_generated", "human_written")]

    summary = plugin.aggregate(results)

    assert summary["confusion_matrix"] == {"tp": 1, "fp": 0, "tn": 0, "fn": 1}
    assert "precision" in summary and "recall" in summary and "f1" in summary


def test_handles_missing_baseline():
    plugin = VeritarachGeneralizationPlugin()  # no baseline supplied
    results = [_result("ai_generated", "ai_generated")]

    summary = plugin.aggregate(results)

    assert summary["baseline_accuracy"] is None
    assert summary["accuracy_delta"] is None
    assert summary["accuracy"] == 1.0


def test_handles_empty_results():
    plugin = VeritarachGeneralizationPlugin(baseline_accuracy=0.9)

    summary = plugin.aggregate([])

    assert summary["accuracy"] is None
    assert summary["accuracy_delta"] is None
