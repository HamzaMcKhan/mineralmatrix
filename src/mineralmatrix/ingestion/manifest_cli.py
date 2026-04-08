from __future__ import annotations

import argparse
from pathlib import Path

from mineralmatrix.ingestion.manifest import build_manifest, write_manifest


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a dataset manifest JSON file.")
    parser.add_argument("--dataset-name", required=True)
    parser.add_argument("--source-name", required=True)
    parser.add_argument("--source-url", required=True)
    parser.add_argument("--local-path", required=True)
    parser.add_argument("--file-format", required=True)
    parser.add_argument("--acquired-date", required=True)
    parser.add_argument("--output-path", required=True)
    parser.add_argument("--declared-crs", default=None)
    parser.add_argument("--inferred-crs", default=None)
    parser.add_argument("--schema-version", default="v1")
    parser.add_argument("--notes", default="")
    parser.add_argument("--known-issue", action="append", default=[])
    return parser.parse_args()


def main() -> Path:
    args = parse_args()

    manifest = build_manifest(
        dataset_name=args.dataset_name,
        source_name=args.source_name,
        source_url=args.source_url,
        local_path=args.local_path,
        file_format=args.file_format,
        declared_crs=args.declared_crs,
        inferred_crs=args.inferred_crs,
        schema_version=args.schema_version,
        acquired_date=args.acquired_date,
        notes=args.notes,
        known_issues=args.known_issue,
    )
    return write_manifest(manifest, args.output_path)


if __name__ == "__main__":
    output = main()
    print(f"Manifest written to: {output}")