from pathlib import Path

from mineralmatrix.ingestion.manifest import DatasetManifest
from mineralmatrix.ingestion.manifest_cli import main


def test_manifest_cli_writes_output(monkeypatch, tmp_path: Path) -> None:
    output_path = tmp_path / "generated_manifest.json"

    argv = [
        "prog",
        "--dataset-name", "nsw_occurrences",
        "--source-name", "NSW Geological Survey",
        "--source-url", "https://example.com/occurrences",
        "--local-path", "data/raw/mineral_occurrences/nsw_occurrences.geojson",
        "--file-format", "geojson",
        "--acquired-date", "2026-04-08",
        "--output-path", str(output_path),
        "--known-issue", "CRS not verified",
        "--known-issue", "Schema not profiled",
    ]

    monkeypatch.setattr("sys.argv", argv)
    result = main()

    assert result == output_path
    assert output_path.exists()

    manifest = DatasetManifest.model_validate_json(output_path.read_text(encoding="utf-8"))
    assert manifest.dataset_name == "nsw_occurrences"
    assert manifest.file_format == "geojson"
    assert manifest.known_issues == ["CRS not verified", "Schema not profiled"]