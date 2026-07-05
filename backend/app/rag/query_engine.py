from backend.app.llm.llm_client import LLMClient
from backend.app.rag.retriever import Retriever
from backend.app.rag.reranker import Reranker
from backend.app.rag.citation_engine import CitationEngine


class QueryEngine:

    def __init__(self):

        self.retriever = Retriever()
        self.reranker = Reranker()
        self.citation_engine = CitationEngine()
        self.llm = LLMClient()

    def ask(
        self,
        question: str,
        system_prompt: str = "",
        top_k: int = 5
    ):

        # Step 1: Retrieve relevant documents
        retrieved_docs = self.retriever.retrieve(
            query=question,
            top_k=10
        )

        # Step 2: Rerank documents
        ranked_docs = self.reranker.rerank(
            retrieved_docs,
            top_k=top_k
        )

        # Step 3: Generate citations
        citations = self.citation_engine.build_citations(
            ranked_docs
        )

        # Step 4: Build context
        context = "\n\n".join(
            doc["text"]
            for doc in ranked_docs
        )

        # Step 5: Build prompt
        prompt = f"""
{system_prompt}

Use ONLY the financial context below to answer the user's question.

If the required information is not present in the context, reply:

"I could not find sufficient evidence in the provided financial documents."

Do not hallucinate.
Do not make assumptions.
Answer in a professional and concise manner.

========================
Financial Context
========================

{context}

========================
User Question
========================

{question}
"""

        # Step 6: Generate response
        answer = self.llm.generate(prompt)

        return {
            "question": question,
            "answer": answer,
            "sources": citations
        }

    def ask_from_context(
        self,
        question: str,
        context: str,
        system_prompt: str = ""
    ):
        """
        Uses an already retrieved context.
        No Pinecone retrieval is performed.
        """

        prompt = f"""
{system_prompt}

Use ONLY the financial context below to answer the user's question.

If the required information is not present in the context, reply:

"I could not find sufficient evidence in the provided financial documents."

Do not hallucinate.
Do not make assumptions.
Answer in a professional and concise manner.

========================
Financial Context
========================

{context}

========================
User Question
========================

{question}
"""

        answer = self.llm.generate(prompt)

        return {
            "question": question,
            "answer": answer
        }