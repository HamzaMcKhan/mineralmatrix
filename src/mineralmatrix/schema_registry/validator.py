from __future__ import annotations

from typing import Any

from mineralmatrix.schema_registry.registry import get_schema


def validate_fields(dataset_name: str, actual_fields: list[str]) -> dict[str, Any]:
    schema = get_schema(dataset_name)

    required_fields = set(schema["required_fields"])
    optional_fields = set(schema["optional_fields"])
    allowed_fields = required_fields | optional_fields

    actual_field_set = set(actual_fields)

    missing_required = sorted(required_fields - actual_field_set)
    unexpected_fields = sorted(actual_field_set - allowed_fields)

    return {
        "dataset_name": dataset_name,
        "missing_required": missing_required,
        "unexpected_fields": unexpected_fields,
        "is_valid": len(missing_required) == 0,
    }