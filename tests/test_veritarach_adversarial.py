from veracia.plugins.veritarach_classifier.adversarial import VeritarachAdversarialPlugin


def _case(original_confidence):
    return {"input": "some paraphrased text", "label": "ai_generated", "original_confidence": original_confidence}


def test_confidence_delta_against_fixture_before_after_pairs():
    plugin = VeritarachAdversarialPlugin()

    result = plugin.score(_case(original_confidence=0.95), {"label": "ai_generated", "confidence": 0.6})

    assert result.metadata["original_confidence"] == 0.95
    assert result.metadata["confidence_delta"] == 0.6 - 0.95


def test_aggregate_reports_pre_and_post_accuracy():
    plugin = VeritarachAdversarialPlugin()
    results = [
        plugin.score(_case(0.9), {"label": "ai_generated", "confidence": 0.7}),  # still correct
        plugin.score(_case(0.85), {"label": "human_written", "confidence": 0.55}),  # flipped by the paraphrase
    ]

    summary = plugin.aggregate(results)

    # every sample started out correctly classified, by construction of the dataset
    assert summary["pre_accuracy"] == 1.0
    # one of the two flipped after paraphrasing
    assert summary["post_accuracy"] == 0.5
    assert summary["avg_confidence_delta"] == ((0.7 - 0.9) + (0.55 - 0.85)) / 2


def test_aggregate_handles_no_results():
    plugin = VeritarachAdversarialPlugin()

    summary = plugin.aggregate([])

    assert summary["pre_accuracy"] is None
    assert summary["post_accuracy"] is None
    assert summary["avg_confidence_delta"] is None
