# app/nodes/csv_reader.py
from typing import TypedDict
import pandas as pd
from rapidfuzz.process_py import extract

from config.settings import CSV_FILE_PATH

class CSVState(TypedDict, total=False):
    raw_data: pd.DataFrame

def read_csv(state: CSVState) -> CSVState:
    df = pd.read_csv(CSV_FILE_PATH)
    state["raw_data"] = df
    return state




------------------

csv located ---xyz location
read csv ---csv_reader node ( panda , pyspark)
schema--- columns extract(
state( df , schema )----llm use (prompt)
pyspark- rectify refinet(prompt llm )
db store
llm final analysis