from backend.app.core.singleton import Singleton


class EmbeddingGenerator:

    def __init__(self):

        self.model = Singleton.embedding_model()

    def generate_embedding(
        self,
        text: str
    ):

        embedding = self.model.encode(
            text,
            normalize_embeddings=True
        )

        return embedding.tolist()

    def generate_embeddings(
        self,
        texts: list[str]
    ):

        embeddings = self.model.encode(
            texts,
            normalize_embeddings=True
        )

        return embeddings.tolist()