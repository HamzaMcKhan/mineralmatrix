from __future__ import annotations

from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field


class DatasetManifest(BaseModel):
    dataset_name: str
    source_name: str
    source_url: str
    local_path: str
    file_format: str
    declared_crs: str | None = None
    inferred_crs: str | None = None
    schema_version: str = "v1"
    acquired_date: str
    notes: str = ""
    known_issues: list[str] = Field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return self.model_dump()


def build_manifest(**kwargs: Any) -> DatasetManifest:
    return DatasetManifest(**kwargs)


def write_manifest(manifest: DatasetManifest, output_path: str | Path) -> Path:
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(manifest.model_dump_json(indent=2), encoding="utf-8")
    return output