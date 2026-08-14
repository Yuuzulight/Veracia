from veracia.core.plugin import EvalResult
from veracia.core.report import render_markdown


def test_markdown_report_generation(tmp_path):
    results = [
        EvalResult(input="q1", expected="A", actual="A", confidence=0.9, metadata={}),
        EvalResult(input="q2", expected="B", actual="C", confidence=0.4, metadata={}),
    ]
    summary = {"accuracy": 0.5}
    out_path = tmp_path / "report.md"

    render_markdown(results, summary, name="Test Run", path=str(out_path))

    content = out_path.read_text(encoding="utf-8")
    assert "# Veracia Eval Report — Test Run" in content
    assert "Dataset: 2 case(s)" in content
    assert "accuracy" in content
    assert "0.5" in content
    assert "q1" in content and "q2" in content


def test_report_includes_worst_n_failures(tmp_path):
    # 12 correct, high-confidence cases plus 3 misclassified, low-confidence ones --
    # the worst section should surface the 3 failures, not just the first 10 rows.
    results = [
        EvalResult(input=f"good-{i}", expected="A", actual="A", confidence=0.95, metadata={})
        for i in range(12)
    ]
    results += [
        EvalResult(input=f"bad-{i}", expected="A", actual="B", confidence=0.1, metadata={})
        for i in range(3)
    ]
    out_path = tmp_path / "report.md"

    render_markdown(results, {}, name="Worst N", path=str(out_path))

    content = out_path.read_text(encoding="utf-8")
    failures_section = content.split("## Failures (worst 10)")[1].split("## Full Results")[0]

    for i in range(3):
        assert f"bad-{i}" in failures_section


def test_report_handles_empty_results(tmp_path):
    out_path = tmp_path / "report.md"

    render_markdown([], {}, name="Empty Run", path=str(out_path))

    content = out_path.read_text(encoding="utf-8")
    assert "Dataset: 0 case(s)" in content
    assert "No results" in content
