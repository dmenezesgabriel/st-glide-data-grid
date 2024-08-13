import os
from typing import List

import pandas as pd
import streamlit.components.v1 as components

from .column_config import BaseColumn

_RELEASE = False


if not _RELEASE:
    _component_func = components.declare_component(
        "glide_data_grid",
        url="http://localhost:5173",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component(
        "glide_data_grid", path=build_dir
    )


def glide_data_grid(
    df: pd.DataFrame, column_config: List[BaseColumn], key=None
):
    data = df.to_dict(orient="records")
    column_config = [config.to_dict() for config in column_config]
    component_value = _component_func(
        data=data, column_config=column_config, key=key
    )
    return component_value
