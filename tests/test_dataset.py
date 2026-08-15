import pytest

from veracia.core.dataset import DatasetError, load_dataset


def _write(tmp_path, name, lines):
    path = tmp_path / name
    path.write_text("\n".join(lines), encoding="utf-8")
    return str(path)


def test_loads_well_formed_file(tmp_path):
    path = _write(
        tmp_path,
        "cases.jsonl",
        ['{"text": "hello", "label": "human"}', '{"text": "world", "label": "ai"}'],
    )

    cases = load_dataset(path, required_fields=["text", "label"])

    assert cases == [
        {"text": "hello", "label": "human"},
        {"text": "world", "label": "ai"},
    ]


def test_raises_on_missing_required_field(tmp_path):
    path = _write(
        tmp_path,
        "cases.jsonl",
        ['{"text": "hello", "label": "human"}', '{"text": "no label here"}'],
    )

    with pytest.raises(DatasetError) as exc_info:
        load_dataset(path, required_fields=["text", "label"])

    message = str(exc_info.value)
    assert "line 2" in message or ":2:" in message
    assert "label" in message


def test_raises_on_missing_file(tmp_path):
    missing_path = str(tmp_path / "does_not_exist.jsonl")

    with pytest.raises(DatasetError):
        load_dataset(missing_path, required_fields=["text"])


def test_empty_file_returns_empty_list(tmp_path):
    path = _write(tmp_path, "empty.jsonl", [])

    assert load_dataset(path, required_fields=["text"]) == []


def test_skips_blank_lines_between_cases(tmp_path):
    path = _write(
        tmp_path,
        "cases.jsonl",
        ['{"text": "hello", "label": "human"}', "", "  ", '{"text": "world", "label": "ai"}'],
    )

    cases = load_dataset(path, required_fields=["text", "label"])

    assert len(cases) == 2


def test_raises_on_malformed_json(tmp_path):
    path = _write(tmp_path, "cases.jsonl", ['{"text": "hello", "label": "human"}', "{not valid json"])

    with pytest.raises(DatasetError) as exc_info:
        load_dataset(path, required_fields=["text", "label"])

    message = str(exc_info.value)
    assert "line 2" in message or ":2:" in message
    assert "invalid JSON" in message
