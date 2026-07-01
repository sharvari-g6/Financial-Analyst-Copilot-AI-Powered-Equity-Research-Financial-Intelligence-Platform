from langchain_text_splitters import RecursiveCharacterTextSplitter


class DocumentChunker:

    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200
    ):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len
        )

    def create_chunks(self, text: str):

        chunks = self.splitter.split_text(text)

        return chunks