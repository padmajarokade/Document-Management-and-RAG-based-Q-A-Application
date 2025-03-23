from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from config import OPENAI_API_KEY
import logging

logger = logging.getLogger(__name__)

async def get_relevant_documents(query, documents, top_n=3):
    try:
        embeddings = OpenAIEmbeddings(api_key=OPENAI_API_KEY)
        vector_store = FAISS.from_documents(documents, embeddings)
        results = vector_store.similarity_search(query, k=top_n)
        return [{"title": doc.metadata["title"], "score": doc.score} for doc in results]
    except Exception as e:
        logger.error(f"Error retrieving documents: {e}")
        return []
