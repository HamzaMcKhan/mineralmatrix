from mineralmatrix.schema_registry.validator import validate_fields


def test_validate_fields_passes_when_required_fields_exist() -> None:
    result = validate_fields(
        "nsw_geology",
        ["geometry", "unit_name", "unit_code", "lithology"],
    )

    assert result["dataset_name"] == "nsw_geology"
    assert result["missing_required"] == []
    assert result["unexpected_fields"] == []
    assert result["is_valid"] is True


def test_validate_fields_flags_missing_required_fields() -> None:
    result = validate_fields(
        "nsw_occurrences",
        ["geometry", "commodity"],
    )

    assert result["missing_required"] == ["occurrence_id"]
    assert result["is_valid"] is False


def test_validate_fields_flags_unexpected_fields() -> None:
    result = validate_fields(
        "synthetic_drillholes",
        ["hole_id", "geometry", "depth_m", "random_field"],
    )

    assert result["missing_required"] == []
    assert result["unexpected_fields"] == ["random_field"]
    assert result["is_valid"] is True