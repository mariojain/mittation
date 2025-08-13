# app/nodes/schema_extractor.py
from typing import TypedDict
import pandas as pd

class SchemaState(TypedDict, total=False):
    raw_data: pd.DataFrame
    schema: list[str]

def extract_schema(state: SchemaState) -> SchemaState:
    df = state.get("raw_data")
    if df is not None:
        state["schema"] = list(df.columns)
    return state
