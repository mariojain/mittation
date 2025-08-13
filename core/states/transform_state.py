# app/nodes/data_transformer.py
from typing import TypedDict
import pandas as pd

class TransformState(TypedDict, total=False):
    raw_data: pd.DataFrame
    transformed_data: pd.DataFrame

def transform_data(state: TransformState) -> TransformState:
    df = state.get("raw_data")
    if df is not None:
        state["transformed_data"] = df.dropna()
    return state
