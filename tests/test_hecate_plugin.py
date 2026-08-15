from veracia.core.plugin import EvalResult
from veracia.plugins.hecate_rag.metrics import HecateRAGPlugin


def _result(faithfulness, relevance):
    return EvalResult(
        input="q",
        expected="expected",
        actual="the answer",
        confidence=faithfulness,
        metadata={"faithfulness": faithfulness, "relevance": relevance},
    )


def test_score_reads_hecates_own_two_metrics():
    plugin = HecateRAGPlugin()
    case = {"question": "What can you tell me about vite?", "context": [], "expected_answer": "..."}
    actual = {"answer": "vite is a build tool", "faithfulness": 0.9, "relevance": 0.8}

    result = plugin.score(case, actual)

    assert result.input == case["question"]
    assert result.actual == "vite is a build tool"
    assert result.confidence == 0.9
    assert result.metadata == {"faithfulness": 0.9, "relevance": 0.8}


def test_hecate_plugin_aggregate_output_shape():
    plugin = HecateRAGPlugin()
    results = [_result(0.9, 0.8), _result(0.7, 0.6), _result(0.2, 0.9)]

    summary = plugin.aggregate(results)

    assert set(summary) == {"avg_faithfulness", "avg_relevance", "pct_hallucination"}
    assert summary["avg_faithfulness"] == (0.9 + 0.7 + 0.2) / 3
    assert summary["avg_relevance"] == (0.8 + 0.6 + 0.9) / 3


def test_hallucination_flag_matches_threshold_at_boundary():
    plugin = HecateRAGPlugin()
    # matches HALLUCINATION_THRESHOLD (0.5) in Hecate's own evaluation.py:
    # strictly below is a hallucination, exactly on the boundary is not.
    results = [_result(0.5, 0.5), _result(0.49999, 0.5)]

    summary = plugin.aggregate(results)

    assert summary["pct_hallucination"] == 0.5


def test_null_faithfulness_does_not_break_the_average():
    # Hecate records a failed metric as null, not zero -- averaging it in as
    # zero would understate the score for reasons that have nothing to do
    # with the answer's quality.
    plugin = HecateRAGPlugin()
    results = [_result(0.9, 0.8), _result(None, None), _result(0.7, 0.6)]

    summary = plugin.aggregate(results)

    assert summary["avg_faithfulness"] == (0.9 + 0.7) / 2
    assert summary["avg_relevance"] == (0.8 + 0.6) / 2
    assert summary["pct_hallucination"] == 0.0


def test_aggregate_handles_all_null_faithfulness():
    plugin = HecateRAGPlugin()
    results = [_result(None, None), _result(None, None)]

    summary = plugin.aggregate(results)

    assert summary["avg_faithfulness"] is None
    assert summary["pct_hallucination"] is None
