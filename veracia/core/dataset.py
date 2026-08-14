import json
from pathlib import Path


class DatasetError(Exception):
    """Raised when a dataset file is missing, malformed, or fails schema validation."""


def load_dataset(path: str, required_fields: list[str]) -> list[dict]:
    file_path = Path(path)
    if not file_path.is_file():
        raise DatasetError(f"Dataset not found: {path}")

    cases = []
    with file_path.open(encoding="utf-8") as f:
        for line_number, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue

            try:
                case = json.loads(line)
            except json.JSONDecodeError as exc:
                raise DatasetError(f"{path}:{line_number}: invalid JSON ({exc})") from exc

            missing = [field for field in required_fields if field not in case]
            if missing:
                raise DatasetError(f"{path}:{line_number}: missing required field(s) {missing}")

            cases.append(case)

    return cases
