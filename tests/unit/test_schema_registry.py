import pytest

from mineralmatrix.schema_registry.registry import get_schema


def test_get_schema_for_geology() -> None:
    schema = get_schema("nsw_geology")
    assert "required_fields" in schema
    assert "geometry" in schema["required_fields"]
    assert schema["geometry_type"] == "polygon"


def test_get_schema_for_occurrences() -> None:
    schema = get_schema("nsw_occurrences")
    assert "occurrence_id" in schema["required_fields"]
    assert schema["geometry_type"] == "point"


def test_get_schema_raises_for_unknown_dataset() -> None:
    with pytest.raises(KeyError):
        get_schema("unknown_dataset")