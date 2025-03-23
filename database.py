import asyncpg
from config import DATABASE_URL

async def get_db_connection():
    return await asyncpg.connect(DATABASE_URL)

async def add_document_to_db(title: str, content: str):
    conn = await get_db_connection()
    await conn.execute("INSERT INTO documents (title, content) VALUES ($1, $2)", title, content)
    await conn.close()

async def get_documents_from_db():
    conn = await get_db_connection()
    rows = await conn.fetch("SELECT title, content FROM documents")
    await conn.close()
    return [{"title": row["title"], "content": row["content"]} for row in rows]
