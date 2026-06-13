# Installation

This document describes the minimal local setup needed to validate and test KTB-300.

## Requirements

- Python `3.10` or newer
- Git
- A terminal with UTF-8 support recommended for Polish content

## 1. Clone the Repository

```bash
git clone https://github.com/Karen86Tonoyan/LLM-Advanced-Reasoning-Hard-Karen-Tonoyan-Benchmark.git
cd LLM-Advanced-Reasoning-Hard-Karen-Tonoyan-Benchmark
```

## 2. Verify Python

```bash
python --version
```

If your system uses `python3`, replace `python` with `python3` in the examples below.

## 3. Validate the JSONL Files

Run validation on all three benchmark sets:

```bash
python scripts/validate_jsonl.py data/ktb_100_en_gold.jsonl
python scripts/validate_jsonl.py data/ktb_100_pl_safety.jsonl
python scripts/validate_jsonl.py data/ktb_100_pl_mix.jsonl
```

Expected result:

```text
Validation passed: 100 records in ...
```

## 4. Test the Evaluation Stub

Prepare a response file, for example `responses.jsonl`:

```json
{"id":"L01","answer":"example answer"}
{"id":"L02","answer":"example answer"}
```

Then run:

```bash
python scripts/run_eval_stub.py data/ktb_100_en_gold.jsonl responses.jsonl
```

The script returns a small JSON report with:

- `total_questions`
- `answered`
- `missing`
- `exact_match_count`
- `exact_match_rate`

## 5. Optional: Rebuild the PL Splits

If you want to regenerate the Polish benchmark files from the local source pack used during development:

```bash
python scripts/build_pl_sets.py
```

This step is optional and only needed when rebuilding the generated PL datasets.

## Troubleshooting

- If Polish characters look broken in PowerShell, switch to UTF-8 before printing files.
- If `python` is not found, install Python and make sure it is added to `PATH`.
- If validation fails, inspect the reported line number and compare the record against `schemas/ktb.schema.json`.
