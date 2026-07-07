from backend.app.core.services import query_engine

from backend.app.graphrag.graph_retriever import GraphRetriever
from backend.app.graphrag.graph_context import GraphContextBuilder


class GraphRAGEngine:

    def __init__(self):

        self.graph = GraphRetriever()

    def ask(
        self,
        company: str,
        question: str
    ):

        # -------------------------------------
        # Retrieve Graph Information
        # -------------------------------------

        graph_data = self.graph.retrieve(company)

        graph_context = GraphContextBuilder.build(
            graph_data
        )

        # -------------------------------------
        # System Prompt
        # -------------------------------------

        system_prompt = f"""
You are an expert Equity Research Analyst.

Answer the user's question using BOTH:

1. Retrieved Financial Documents
2. Knowledge Graph Information

Knowledge Graph

{graph_context}

Rules

- Combine information from both sources.
- Do not hallucinate.
- If graph information supports the retrieved documents,
mention it.
- Produce a concise but informative answer.
"""

        # -------------------------------------
        # Query Engine (Pinecone + LLM)
        # -------------------------------------

        result = query_engine.ask(

            question=question,

            system_prompt=system_prompt,

            top_k=10

        )

        return result