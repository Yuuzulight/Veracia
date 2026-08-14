import pytest

from veracia.core.plugin import EvalResult, MetricPlugin


class _StubPlugin(MetricPlugin):
    def score(self, case, actual):
        return EvalResult(
            input=case["input"],
            expected=case.get("expected"),
            actual=actual,
            confidence=1.0,
            metadata={},
        )

    def aggregate(self, results):
        return {"count": len(results)}


def test_concrete_subclass_scores_and_aggregates():
    plugin = _StubPlugin()
    result = plugin.score({"input": "x", "expected": "y"}, "y")

    assert result == EvalResult(input="x", expected="y", actual="y", confidence=1.0, metadata={})
    assert plugin.aggregate([result]) == {"count": 1}


def test_subclass_missing_aggregate_cannot_instantiate():
    class _MissingAggregate(MetricPlugin):
        def score(self, case, actual):
            return EvalResult(input=None, expected=None, actual=None, confidence=None, metadata={})

    with pytest.raises(TypeError):
        _MissingAggregate()


def test_subclass_missing_score_cannot_instantiate():
    class _MissingScore(MetricPlugin):
        def aggregate(self, results):
            return {}

    with pytest.raises(TypeError):
        _MissingScore()
