from veracia.core.plugin import EvalResult, MetricPlugin
from veracia.core.runner import Runner


class _RecordingPlugin(MetricPlugin):
    def __init__(self):
        self.scored_calls = []

    def score(self, case, actual):
        self.scored_calls.append((case, actual))
        return EvalResult(input=case["input"], expected=case.get("expected"), actual=actual, confidence=1.0, metadata={})

    def aggregate(self, results):
        return {"count": len(results)}


def test_runner_calls_plugin_score_per_case():
    plugin = _RecordingPlugin()
    dataset = [{"input": "a", "expected": "A"}, {"input": "b", "expected": "B"}]
    runner = Runner(predict_fn=lambda x: x.upper(), metric_plugin=plugin)

    results = runner.run(dataset)

    assert len(results) == 2
    assert plugin.scored_calls == [
        ({"input": "a", "expected": "A"}, "A"),
        ({"input": "b", "expected": "B"}, "B"),
    ]


def test_runner_preserves_case_order():
    plugin = _RecordingPlugin()
    dataset = [{"input": str(i)} for i in range(10)]
    runner = Runner(predict_fn=lambda x: x, metric_plugin=plugin)

    results = runner.run(dataset)

    assert [r.input for r in results] == [str(i) for i in range(10)]


def test_runner_handles_predict_fn_exception():
    plugin = _RecordingPlugin()

    def flaky_predict(x):
        if x == "bad":
            raise ValueError("boom")
        return x.upper()

    dataset = [{"input": "good", "expected": "GOOD"}, {"input": "bad"}, {"input": "also_good", "expected": "ALSO_GOOD"}]
    runner = Runner(predict_fn=flaky_predict, metric_plugin=plugin)

    results = runner.run(dataset)

    assert len(results) == 3
    assert results[0].actual == "GOOD"
    assert results[1].actual is None
    assert "boom" in results[1].metadata["error"]
    assert results[2].actual == "ALSO_GOOD"
    # the failing case never reached the plugin
    assert len(plugin.scored_calls) == 2
