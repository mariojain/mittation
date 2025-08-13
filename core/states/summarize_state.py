# app/nodes/gemini_summarizer.py
from typing import TypedDict
import pandas as pd
from core.llm.gemini import llm
from langchain_core.messages import HumanMessage

class SummarizeState(TypedDict, total=False):
    transformed_data: pd.DataFrame
    gemini_output: str

def summarize_data(state: SummarizeState) -> SummarizeState:
    df = state.get("transformed_data")
    if df is not None:
        prompt = f"Summarize the following NYC housing data:\n{df.head(3).to_string(index=False)}"
        response = llm.invoke([HumanMessage(content=prompt)])
        state["gemini_output"] = response.content
    return state
