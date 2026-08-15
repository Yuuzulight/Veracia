import responses

from veracia.core.plugin import EvalResult
from veracia.plugins.veritarach_classifier.client import DEFAULT_BASE_URL, predict
from veracia.plugins.veritarach_classifier.metrics import VeritarachClassifierPlugin


def _result(expected, actual):
    return EvalResult(input="...", expected=expected, actual=actual, confidence=0.9, metadata={})


def test_confusion_matrix_arithmetic():
    plugin = VeritarachClassifierPlugin()
    results = [
        _result("ai_generated", "ai_generated"),  # tp
        _result("ai_generated", "ai_generated"),  # tp
        _result("human_written", "ai_generated"),  # fp
        _result("human_written", "human_written"),  # tn
        _result("ai_generated", "human_written"),  # fn
    ]

    summary = plugin.aggregate(results)
    matrix = summary["confusion_matrix"]

    assert matrix == {"tp": 2, "fp": 1, "tn": 1, "fn": 1}
    assert sum(matrix.values()) == len(results)
    assert summary["precision"] == 2 / 3
    assert summary["recall"] == 2 / 3
    assert summary["false_positive_rate"] == 0.5


def test_precision_recall_zero_division_handled():
    plugin = VeritarachClassifierPlugin()
    # no positive predictions at all -- precision would otherwise divide by zero
    results = [_result("ai_generated", "human_written"), _result("human_written", "human_written")]

    summary = plugin.aggregate(results)

    assert summary["precision"] == 0.0
    assert summary["recall"] == 0.0
    assert summary["f1"] == 0.0


def test_score_truncates_long_input_for_the_report():
    plugin = VeritarachClassifierPlugin()
    long_text = "x" * 200
    case = {"input": long_text, "label": "ai_generated"}
    actual = {"label": "ai_generated", "confidence": 0.87}

    result = plugin.score(case, actual)

    assert result.input == "x" * 100 + "..."
    assert result.expected == "ai_generated"
    assert result.actual == "ai_generated"
    assert result.confidence == 0.87
    assert result.metadata == {"correct": True}


@responses.activate
def test_predict_calls_the_deployed_endpoint():
    responses.add(
        responses.POST,
        f"{DEFAULT_BASE_URL}/predict",
        json={"label": "human_written", "confidence": 0.73},
        status=200,
    )

    result = predict("some text to classify")

    assert result == {"label": "human_written", "confidence": 0.73}
    assert responses.calls[0].request.url == f"{DEFAULT_BASE_URL}/predict"
