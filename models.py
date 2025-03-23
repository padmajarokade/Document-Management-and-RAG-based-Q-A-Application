from pydantic import BaseModel

class DocumentRequest(BaseModel):
    title: str
    content: str

class QueryRequest(BaseModel):
    query: str
