from fastapi import FastAPI, HTTPException, Depends
from database import add_document_to_db, get_documents_from_db
from retrieval import get_relevant_documents
from models import DocumentRequest, QueryRequest
import logging

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.post("/add-document/")
async def add_document(request: DocumentRequest):
    try:
        await add_document_to_db(request.title, request.content)
        return {"message": "Document added successfully!"}
    except Exception as e:
        logger.error(f"Error adding document: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/documents/")
async def list_documents():
    try:
        return await get_documents_from_db()
    except Exception as e:
        logger.error(f"Error fetching documents: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.post("/ask/")
async def ask_question(request: QueryRequest):
    try:
        documents = await get_documents_from_db()
        relevant_docs = await get_relevant_documents(request.query, documents)
        return {"query": request.query, "relevant_documents": relevant_docs}
    except Exception as e:
        logger.error(f"Error processing query: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
