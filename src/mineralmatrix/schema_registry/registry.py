from __future__ import annotations

from typing import Any


CANONICAL_SCHEMAS: dict[str, dict[str, Any]] = {
    "nsw_geology": {
        "required_fields": [
            "geometry",
            "unit_name",
            "unit_code",
        ],
        "optional_fields": [
            "group_name",
            "lithology",
            "age",
        ],
        "geometry_type": "polygon",
    },
    "nsw_occurrences": {
        "required_fields": [
            "geometry",
            "occurrence_id",
            "commodity",
        ],
        "optional_fields": [
            "deposit_type",
            "status",
            "source",
        ],
        "geometry_type": "point",
    },
    "synthetic_drillholes": {
        "required_fields": [
            "hole_id",
            "geometry",
            "depth_m",
        ],
        "optional_fields": [
            "azimuth",
            "dip",
            "campaign_id",
        ],
        "geometry_type": "point",
    },
}


def get_schema(dataset_name: str) -> dict[str, Any]:
    return CANONICAL_SCHEMAS[dataset_name]