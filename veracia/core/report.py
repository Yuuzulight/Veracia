from pathlib import Path

from veracia.core.plugin import EvalResult

_WORST_N = 10


def _badness(result: EvalResult):
    is_wrong = result.expected is not None and result.actual != result.expected
    confidence = result.confidence if result.confidence is not None else 0.0
    return (0 if is_wrong else 1, confidence)


def _summary_table(summary: dict) -> str:
    if not summary:
        return "_No summary statistics._"
    lines = ["| Metric | Value |", "| --- | --- |"]
    lines.extend(f"| {key} | {value} |" for key, value in summary.items())
    return "\n".join(lines)


def _results_table(results: list[EvalResult]) -> str:
    if not results:
        return "_No results._"
    lines = ["| Input | Expected | Actual | Confidence |", "| --- | --- | --- | --- |"]
    lines.extend(f"| {r.input!r} | {r.expected!r} | {r.actual!r} | {r.confidence} |" for r in results)
    return "\n".join(lines)


def render_markdown(results: list[EvalResult], summary: dict, name: str, path: str) -> None:
    worst = sorted(results, key=_badness)[:_WORST_N]

    content = "\n\n".join(
        [
            f"# Veracia Eval Report — {name}",
            f"Dataset: {len(results)} case(s)",
            "## Summary",
            _summary_table(summary),
            "## Failures (worst 10)",
            _results_table(worst),
            "## Full Results",
            _results_table(results),
        ]
    )

    Path(path).write_text(content + "\n", encoding="utf-8")
