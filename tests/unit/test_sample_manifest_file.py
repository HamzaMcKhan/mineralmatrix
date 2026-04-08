import json
from pathlib import Path


def test_sample_geology_manifest_exists() -> None:
    manifest_path = Path("data/manifests/geology/nsw_geology_manifest.json")
    assert manifest_path.exists()


def test_sample_geology_manifest_has_required_keys() -> None:
    manifest_path = Path("data/manifests/geology/nsw_geology_manifest.json")
    data = json.loads(manifest_path.read_text(encoding="utf-8"))

    required_keys = {
        "dataset_name",
        "source_name",
        "source_url",
        "local_path",
        "file_format",
        "declared_crs",
        "inferred_crs",
        "schema_version",
        "acquired_date",
        "notes",
        "known_issues",
    }

    assert required_keys.issubset(data.keys())
    assert data["dataset_name"] == "nsw_geology"