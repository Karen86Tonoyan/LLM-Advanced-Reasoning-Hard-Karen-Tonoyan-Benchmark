from __future__ import annotations

import json
import sys
from pathlib import Path


REQUIRED_FIELDS = {
    "id": str,
    "set": str,
    "category": str,
    "difficulty": int,
    "question": str,
    "gold_answer": str,
    "tags": list,
    "mono": str,
}


def validate_record(record: dict, line_no: int) -> list[str]:
    errors: list[str] = []
    for field, field_type in REQUIRED_FIELDS.items():
        if field not in record:
            errors.append(f"line {line_no}: missing field '{field}'")
            continue
        if not isinstance(record[field], field_type):
            errors.append(
                f"line {line_no}: field '{field}' must be {field_type.__name__}, got {type(record[field]).__name__}"
            )

    if "difficulty" in record and isinstance(record["difficulty"], int):
        if not 1 <= record["difficulty"] <= 5:
            errors.append(f"line {line_no}: difficulty must be in range 1..5")

    if "tags" in record and isinstance(record["tags"], list):
        if not record["tags"]:
            errors.append(f"line {line_no}: tags must not be empty")
        elif any(not isinstance(tag, str) or not tag.strip() for tag in record["tags"]):
            errors.append(f"line {line_no}: every tag must be a non-empty string")

    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/validate_jsonl.py data/file.jsonl")
        return 2

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"File not found: {path}")
        return 2

    errors: list[str] = []
    count = 0
    for line_no, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw_line.strip()
        if not line:
            continue
        count += 1
        try:
            record = json.loads(line)
        except json.JSONDecodeError as exc:
            errors.append(f"line {line_no}: invalid json ({exc})")
            continue
        if not isinstance(record, dict):
            errors.append(f"line {line_no}: record must be a JSON object")
            continue
        errors.extend(validate_record(record, line_no))

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validation passed: {count} records in {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
