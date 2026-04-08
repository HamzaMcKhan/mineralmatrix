import pandas as pd

from mineralmatrix.standardization.drillholes import standardize_drillholes


def test_standardize_v1_keeps_columns() -> None:
    df = pd.DataFrame(
        {
            "hole_id": ["DH001"],
            "x": [145.8],
            "y": [-31.4],
            "depth_m": [200],
            "azimuth": [90],
            "dip": [-60],
            "campaign_id": ["A"],
        }
    )

    result = standardize_drillholes(df)

    assert "hole_id" in result.columns
    assert "x" in result.columns
    assert len(result.columns) == 7


def test_standardize_v2_maps_columns() -> None:
    df = pd.DataFrame(
        {
            "drillhole_id": ["DH005"],
            "x_coord": [145.9],
            "y_coord": [-31.5],
            "depth_meters": [210],
            "azimuth": [95],
            "dip_deg": [-58],
            "campaign": ["B"],
        }
    )

    result = standardize_drillholes(df)

    assert "hole_id" in result.columns
    assert "x" in result.columns
    assert "y" in result.columns
    assert "depth_m" in result.columns
    assert "dip" in result.columns
    assert "campaign_id" in result.columns