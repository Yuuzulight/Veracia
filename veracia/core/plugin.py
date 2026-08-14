from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass
class EvalResult:
    input: Any
    expected: Any
    actual: Any
    confidence: float | None
    metadata: dict


class MetricPlugin(ABC):
    @abstractmethod
    def score(self, case: dict, actual: Any) -> EvalResult:
        """Score a single prediction against its expected case."""

    @abstractmethod
    def aggregate(self, results: list[EvalResult]) -> dict:
        """Compute summary statistics across all results."""
