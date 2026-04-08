from __future__ import annotations

import pandas as pd


COLUMN_MAPPING_V2 = {
    "drillhole_id": "hole_id",
    "x_coord": "x",
    "y_coord": "y",
    "depth_meters": "depth_m",
    "dip_deg": "dip",
    "campaign": "campaign_id",
}


def standardize_drillholes(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # detect schema version
    if "hole_id" in df.columns:
        # already v1
        standardized = df
    else:
        # assume v2 → map columns
        standardized = df.rename(columns=COLUMN_MAPPING_V2)

    return standardized