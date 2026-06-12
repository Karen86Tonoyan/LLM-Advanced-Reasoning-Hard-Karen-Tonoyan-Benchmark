# Karen Tonoyan Benchmark (KTB-300)

KTB-300 is a benchmark pack with 300 hard questions for evaluating large language models on reasoning quality, uncertainty handling, hallucination resistance, safety, planning, ambiguity handling, and consistency.

For a styled visual overview, open `docs/landing.html` locally in a browser.

The repository currently contains:

- `100` EN gold-answer reasoning questions
- `100` PL safety / hallucination / epistemic questions
- `100` PL mixed reasoning / math / planning / meta questions
- a JSONL validation script
- a lightweight evaluation stub
- scoring rubric and category notes

## Repository Layout

```text
data/
  ktb_100_en_gold.jsonl
  ktb_100_pl_safety.jsonl
  ktb_100_pl_mix.jsonl

docs/
  categories.md
  installation.md
  landing.html
  rubric.md

schemas/
  ktb.schema.json

scripts/
  build_pl_sets.py
  run_eval_stub.py
  validate_jsonl.py
```

## Dataset Format

Each JSONL record follows the same compact structure:

```json
{
  "id": "L01",
  "set": "EN-GOLD",
  "category": "Logic",
  "difficulty": 5,
  "question": "...",
  "gold_answer": "...",
  "tags": ["logic", "contradiction"],
  "mono": "BENCH:KTB300 CAT:LOGIC"
}
```

## Quick Start

Requirements:

- Python `3.10+`
- Git

Clone the repository:

```bash
git clone https://github.com/Karen86Tonoyan/LLM-Advanced-Reasoning-Hard-Karen-Tonoyan-Benchmark.git
cd LLM-Advanced-Reasoning-Hard-Karen-Tonoyan-Benchmark
```

Validate each dataset split:

```bash
python scripts/validate_jsonl.py data/ktb_100_en_gold.jsonl
python scripts/validate_jsonl.py data/ktb_100_pl_safety.jsonl
python scripts/validate_jsonl.py data/ktb_100_pl_mix.jsonl
```

Run a simple exact-match evaluation:

```bash
python scripts/run_eval_stub.py data/ktb_100_en_gold.jsonl responses.jsonl
```

`responses.jsonl` should contain records like:

```json
{"id":"L01","answer":"..."}
```

## How to Evaluate

1. Run your model against the `question` field in one of the dataset files.
2. For `EN-GOLD`, compare generated answers against `gold_answer`.
3. For `PL-SAFETY` and `PL-MIX`, use the rubric in `docs/rubric.md` for manual scoring.

## Documentation

- Installation and setup: [docs/installation.md](docs/installation.md)
- Scoring rubric: [docs/rubric.md](docs/rubric.md)
- Category overview: [docs/categories.md](docs/categories.md)
- Styled landing page: [docs/landing.html](docs/landing.html)

## Notes

- `run_eval_stub.py` is intentionally minimal and currently checks exact match only.
- For manual scoring, use the rubric in `docs/rubric.md`.
- The `mono` field is reserved for compact semantic tagging and benchmark metadata.
