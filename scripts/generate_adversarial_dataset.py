"""Generates datasets/veritarach_adversarial.jsonl.

Takes the ai_generated rows from the holdout set that Veritarach already
classifies correctly, paraphrases each one through an OpenAI-compatible
/chat/completions endpoint, and records the pre-perturbation confidence
alongside the paraphrased text so the adversarial plugin can compute a
before/after delta without needing to re-run the original samples itself.

Usage:
    python scripts/generate_adversarial_dataset.py --base-url http://localhost:8080/v1
"""

import argparse
import json
import sys

import requests

from veracia.core.dataset import load_dataset
from veracia.plugins.veritarach_classifier.client import predict as veritarach_predict

PARAPHRASE_PROMPT = (
    "Paraphrase the following text. Keep the same meaning and roughly the same "
    "length, but use different sentence structure and word choices. Return only "
    "the paraphrased text, nothing else.\n\n{text}"
)


def paraphrase(base_url: str, text: str, model: str) -> str:
    response = requests.post(
        f"{base_url}/chat/completions",
        json={
            "model": model,
            "messages": [{"role": "user", "content": PARAPHRASE_PROMPT.format(text=text)}],
            "max_tokens": 400,
            "temperature": 0.8,
        },
        timeout=120,
    )
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"].strip()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", required=True, help="OpenAI-compatible base URL for the paraphraser")
    parser.add_argument("--model", default="local-model")
    parser.add_argument("--holdout", default="datasets/veritarach_holdout_test.jsonl")
    parser.add_argument("--out", default="datasets/veritarach_adversarial.jsonl")
    args = parser.parse_args()

    holdout = load_dataset(args.holdout, required_fields=["input", "label"])
    ai_rows = [row for row in holdout if row["label"] == "ai_generated"]

    written = 0
    with open(args.out, "w", encoding="utf-8") as f:
        for i, row in enumerate(ai_rows, start=1):
            original = veritarach_predict(row["input"])
            if original["label"] != "ai_generated":
                print(f"[{i}/{len(ai_rows)}] skipped (already misclassified)", file=sys.stderr)
                continue

            paraphrased_text = paraphrase(args.base_url, row["input"], args.model)
            f.write(
                json.dumps(
                    {
                        "input": paraphrased_text,
                        "label": "ai_generated",
                        "original_confidence": original["confidence"],
                    },
                    ensure_ascii=False,
                )
                + "\n"
            )
            f.flush()
            written += 1
            print(f"[{i}/{len(ai_rows)}] paraphrased", file=sys.stderr)

    print(f"wrote {written} rows", file=sys.stderr)


if __name__ == "__main__":
    main()
