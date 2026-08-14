from typing import Any, Callable

from veracia.core.plugin import EvalResult, MetricPlugin


class Runner:
    def __init__(self, predict_fn: Callable[[Any], Any], metric_plugin: MetricPlugin):
        self.predict_fn = predict_fn
        self.plugin = metric_plugin

    def run(self, dataset: list[dict]) -> list[EvalResult]:
        results = []
        for case in dataset:
            try:
                actual = self.predict_fn(case["input"])
            except Exception as exc:
                results.append(
                    EvalResult(
                        input=case.get("input"),
                        expected=case.get("expected"),
                        actual=None,
                        confidence=None,
                        metadata={"error": str(exc)},
                    )
                )
                continue

            results.append(self.plugin.score(case, actual))

        return results
