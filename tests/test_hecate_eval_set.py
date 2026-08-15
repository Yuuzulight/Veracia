from veracia.plugins.hecate_rag.eval_set import load_hecate_eval_set


def test_loads_the_committed_seed_set():
    cases = load_hecate_eval_set("datasets/hecate_eval_qa.jsonl")

    assert len(cases) == 12
    for case in cases:
        assert "question" in case
        assert "context" in case
        assert "expected_answer" in case

    ids = {case["id"] for case in cases}
    assert "growth-seven-day" in ids  # the 7-day refusal trap
    assert "trap-outside-dataset" in ids
