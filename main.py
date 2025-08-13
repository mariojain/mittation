from google.genai.types import Image

from core.graph_builder import build_graph
from core.graph_builder import get_uncompiled_graph
from IPython.display import display,Image





if __name__ == "__main__":
    print("🧭 Mermaid Graph:")
    graph = build_graph()
    display(Image(graph.get_graph().draw_mermaid_png()))


    final_state = graph.invoke({})  # Empty dict = initial state

    print("\n✅ Final Output:")
    for k, v in final_state.items():
        print(f"{k}:", v if not hasattr(v, 'head') else v.head(2).to_string(index=False))  # Pretty print DataFrames
