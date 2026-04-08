from pathlib import Path

import pandas as pd


def test_synthetic_drillholes_v1_exists_and_has_expected_columns() -> None:
    file_path = Path("data/synthetic/synthetic_drillholes_v1.csv")
    assert file_path.exists()

    df = pd.read_csv(file_path)

    expected_columns = [
        "hole_id",
        "x",
        "y",
        "depth_m",
        "azimuth",
        "dip",
        "campaign_id",
    ]
    assert list(df.columns) == expected_columns
    assert len(df) == 4


def test_synthetic_drillholes_v2_exists_and_has_schema_variation() -> None:
    file_path = Path("data/synthetic/synthetic_drillholes_v2.csv")
    assert file_path.exists()

    df = pd.read_csv(file_path)

    expected_columns = [
        "drillhole_id",
        "x_coord",
        "y_coord",
        "depth_meters",
        "azimuth",
        "dip_deg",
        "campaign",
    ]
    assert list(df.columns) == expected_columns
    assert len(df) == 3