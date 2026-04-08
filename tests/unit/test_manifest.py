import json
from pathlib import Path

from mineralmatrix.ingestion.manifest import DatasetManifest, build_manifest, write_manifest


def test_build_manifest_returns_model() -> None:
    manifest = build_manifest(
        dataset_name="nsw_geology",
        source_name="NSW Geological Survey",
        source_url="https://example.com/geology",
        local_path="data/raw/geology/nsw_geology.gpkg",
        file_format="gpkg",
        declared_crs="EPSG:4326",
        inferred_crs="EPSG:4326",
        acquired_date="2026-04-08",
    )

    assert isinstance(manifest, DatasetManifest)
    assert manifest.dataset_name == "nsw_geology"
    assert manifest.schema_version == "v1"


def test_write_manifest_creates_json_file(tmp_path: Path) -> None:
    manifest = build_manifest(
        dataset_name="nsw_geology",
        source_name="NSW Geological Survey",
        source_url="https://example.com/geology",
        local_path="data/raw/geology/nsw_geology.gpkg",
        file_format="gpkg",
        declared_crs="EPSG:4326",
        inferred_crs="EPSG:4326",
        acquired_date="2026-04-08",
    )

    output_file = tmp_path / "manifest.json"
    write_manifest(manifest, output_file)

    assert output_file.exists()

    data = json.loads(output_file.read_text(encoding="utf-8"))
    assert data["dataset_name"] == "nsw_geology"
    assert data["file_format"] == "gpkg"