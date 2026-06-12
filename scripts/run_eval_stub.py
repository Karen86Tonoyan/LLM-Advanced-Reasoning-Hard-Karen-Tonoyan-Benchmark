from __future__ import annotations

import json
import sys
from pathlib import Path


def normalize(text: str) -> str:
    return " ".join(text.strip().lower().split())


def load_jsonl(path: Path) -> list[dict]:
    rows: list[dict] = []
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if line:
            rows.append(json.loads(line))
    return rows


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: python scripts/run_eval_stub.py data/benchmark.jsonl responses.jsonl")
        return 2

    benchmark_path = Path(sys.argv[1])
    responses_path = Path(sys.argv[2])

    if not benchmark_path.exists() or not responses_path.exists():
        print("Benchmark file or responses file does not exist.")
        return 2

    benchmark_rows = load_jsonl(benchmark_path)
    response_rows = load_jsonl(responses_path)
    response_map = {row["id"]: row for row in response_rows if "id" in row}

    scored = 0
    exact_match = 0
    missing = 0

    for item in benchmark_rows:
        response = response_map.get(item["id"])
        if response is None:
            missing += 1
            continue
        scored += 1
        model_answer = normalize(str(response.get("answer", "")))
        gold_answer = normalize(item["gold_answer"])
        if model_answer == gold_answer:
            exact_match += 1

    total = len(benchmark_rows)
    print(
        json.dumps(
            {
                "benchmark_file": str(benchmark_path),
                "responses_file": str(responses_path),
                "total_questions": total,
                "answered": scored,
                "missing": missing,
                "exact_match_count": exact_match,
                "exact_match_rate": round(exact_match / total, 4) if total else 0.0,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
