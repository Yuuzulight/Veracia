"""Runs all three Veritarach checks against the live deployment and writes
the reports to docs/examples/, as committed snapshots rather than the
gitignored reports/ directory used for regenerable local runs.

Usage:
    python scripts/generate_example_reports.py
"""

from veracia.core.dataset import load_dataset
from veracia.core.report import render_markdown
from veracia.core.runner import Runner
from veracia.plugins.veritarach_classifier.adversarial import VeritarachAdversarialPlugin
from veracia.plugins.veritarach_classifier.client import predict
from veracia.plugins.veritarach_classifier.generalization import VeritarachGeneralizationPlugin
from veracia.plugins.veritarach_classifier.metrics import VeritarachClassifierPlugin


def run(dataset_path, plugin, name, out_path):
    dataset = load_dataset(dataset_path, required_fields=["input", "label"])
    runner = Runner(predict_fn=predict, metric_plugin=plugin)
    results = runner.run(dataset)
    summary = plugin.aggregate(results)
    render_markdown(results, summary, name=name, path=out_path)
    return summary


def main():
    holdout_summary = run(
        "datasets/veritarach_holdout_test.jsonl",
        VeritarachClassifierPlugin(),
        "Veritarach holdout",
        "docs/examples/veritarach_holdout.md",
    )
    matrix = holdout_summary["confusion_matrix"]
    holdout_accuracy = (matrix["tp"] + matrix["tn"]) / sum(matrix.values())
    print(f"holdout: {holdout_summary}")

    generalization_summary = run(
        "datasets/veritarach_cross_model.jsonl",
        VeritarachGeneralizationPlugin(baseline_accuracy=holdout_accuracy),
        "Veritarach cross-model generalization",
        "docs/examples/veritarach_generalization.md",
    )
    print(f"generalization: {generalization_summary}")

    adversarial_summary = run(
        "datasets/veritarach_adversarial.jsonl",
        VeritarachAdversarialPlugin(),
        "Veritarach adversarial robustness",
        "docs/examples/veritarach_adversarial.md",
    )
    print(f"adversarial: {adversarial_summary}")


if __name__ == "__main__":
    main()
