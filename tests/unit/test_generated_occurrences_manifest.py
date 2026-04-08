import json
from pathlib import Path


def test_generated_occurrences_manifest_exists() -> None:
    manifest_path = Path(
        "data/manifests/mineral_occurrences/nsw_occurrences_manifest.json"
    )
    assert manifest_path.exists()


def test_generated_occurrences_manifest_content() -> None:
    manifest_path = Path(
        "data/manifests/mineral_occurrences/nsw_occurrences_manifest.json"
    )
    data = json.loads(manifest_path.read_text(encoding="utf-8"))

    assert data["dataset_name"] == "nsw_occurrences"
    assert data["file_format"] == "geojson"
    assert len(data["known_issues"]) == 3