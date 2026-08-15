"""Generates datasets/veritarach_cross_model.jsonl.

Calls any OpenAI-compatible /chat/completions endpoint to produce short text
samples, labeled ai_generated. The point is to test Veritarach against a model
genuinely absent from its training mix (Claude, GPT-4o, Gemini, HC3) -- this
script doesn't care which model that is, it just needs an OpenAI-compatible
endpoint pointed at one. Run against a local llama-server instance, for
example, with no API key or new account required.

Usage:
    python scripts/generate_cross_model_dataset.py --base-url http://localhost:8080/v1
"""

import argparse
import itertools
import json
import sys

import requests

TOPICS = [
    "the history of tea",
    "how bicycles balance while moving",
    "why leaves change color in autumn",
    "the difference between weather and climate",
    "how a lighthouse works",
    "the invention of the printing press",
    "why bread rises",
    "how noise-cancelling headphones work",
    "the migration patterns of monarch butterflies",
    "how a thermostat regulates temperature",
    "the origin of chess",
    "why the sky is blue",
    "how compost breaks down",
    "the history of the bicycle",
    "how tides are caused by the moon",
    "why cats purr",
    "the basics of how a battery stores energy",
    "how bread is made in a bakery",
    "the history of coffee",
    "how a violin produces sound",
]

STYLES = [
    "a short informative paragraph, about 120 words",
    "a brief, casual personal note about the topic, about 100 words",
    "a short story opening that touches on the topic, about 100 words",
    "a few practical tips related to the topic, about 120 words",
    "a short news-style summary about the topic, about 100 words",
]


def build_prompts():
    return [
        f"Write {style}: {topic}."
        for topic, style in itertools.product(TOPICS, STYLES)
    ]


def generate_one(base_url: str, prompt: str, model: str) -> str:
    response = requests.post(
        f"{base_url}/chat/completions",
        json={
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 300,
            "temperature": 0.9,
        },
        timeout=120,
    )
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"].strip()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", required=True, help="OpenAI-compatible base URL, e.g. http://localhost:8080/v1")
    parser.add_argument("--model", default="local-model", help="model name to send in the request body")
    parser.add_argument("--out", default="datasets/veritarach_cross_model.jsonl")
    parser.add_argument("--limit", type=int, default=None, help="cap the number of prompts, mostly for testing")
    args = parser.parse_args()

    prompts = build_prompts()
    if args.limit:
        prompts = prompts[: args.limit]

    with open(args.out, "w", encoding="utf-8") as f:
        for i, prompt in enumerate(prompts, start=1):
            text = generate_one(args.base_url, prompt, args.model)
            f.write(json.dumps({"input": text, "label": "ai_generated"}, ensure_ascii=False) + "\n")
            f.flush()
            print(f"[{i}/{len(prompts)}] generated", file=sys.stderr)


if __name__ == "__main__":
    main()
