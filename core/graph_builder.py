# app/core/graph_builder.py

from langgraph.graph import StateGraph, END

# Import node functions


from core.states.csv_state import read_csv
from core.states.schema_state import extract_schema
from core.states.transform_state import transform_data
from core.states.summarize_state import  summarize_data

# Optional: Union of all states
from typing import TypedDict
import pandas as pd

class GraphState(TypedDict, total=False):
    raw_data: pd.DataFrame
    schema: list[str]
    transformed_data: pd.DataFrame
    gemini_output: str

def get_uncompiled_graph():
    builder = StateGraph(GraphState)

    # Add nodes
    builder.add_node("read_csv", read_csv)
    builder.add_node("extract_schema", extract_schema)
    builder.add_node("transform_data", transform_data)
    builder.add_node("summarize_data", summarize_data)

    # Define flow
    builder.set_entry_point("read_csv")
    builder.add_edge("read_csv", "extract_schema")
    builder.add_edge("extract_schema", "transform_data")
    builder.add_edge("transform_data", "summarize_data")
    builder.add_edge("summarize_data", END)

    return builder

def build_graph():
    return get_uncompiled_graph().compile()
