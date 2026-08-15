from veracia.core.dataset import load_dataset

REQUIRED_FIELDS = ["question", "context", "expected_answer"]


def load_hecate_eval_set(path: str) -> list[dict]:
    return load_dataset(path, required_fields=REQUIRED_FIELDS)
