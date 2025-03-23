# Document-Management-and-RAG-based-Q-A-Application
A scalable Retrieval-Augmented Generation (RAG)-based Q&A system using FastAPI, PostgreSQL, and LLM embeddings.  

## 🚀 Features  
- **LLM-based Document Retrieval** (OpenAI Embeddings + FAISS)  
- **Asynchronous API** for better performance  
- **PostgreSQL Database** for structured storage  
- **Error handling & logging** for reliability  

## 📌 Installation  
### 1️⃣ Clone the repository  
```sh
git clone https://github.com/YOUR_USERNAME/RAG-Document-QA.git
cd RAG-Document-QA
```  

### 2️⃣ Install dependencies  
```sh
pip install -r requirements.txt
```  

### 3️⃣ Set up PostgreSQL  
```sh
CREATE DATABASE rag_db;
```  

### 4️⃣ Set up environment variables  
Create a `.env` file in the project root and add:  
```
DATABASE_URL=postgresql://user:password@localhost:5432/rag_db
OPENAI_API_KEY=your_openai_api_key
```  

### 5️⃣ Run the API  
```sh
uvicorn main:app --reload
```  

## 📡 API Endpoints  
| Method | Endpoint | Description |  
|--------|---------|-------------|  
| **POST** | `/add-document/` | Add a new document |  
| **GET** | `/documents/` | List all stored documents |  
| **POST** | `/ask/` | Ask a question and retrieve relevant documents |  

## 💡 Example Usage  
### **1️⃣ Add a Document**  
```sh
curl -X POST "http://127.0.0.1:8000/add-document/" -H "Content-Type: application/json" -d '{"title": "AI", "content": "AI is changing the world."}'
```  

### **2️⃣ List All Documents**  
```sh
curl -X GET "http://127.0.0.1:8000/documents/"
```  

### **3️⃣ Ask a Question**  
```sh
curl -X POST "http://127.0.0.1:8000/ask/" -H "Content-Type: application/json" -d '{"query": "What is AI?"}'
```  

## 🛠️ Tech Stack  
- **FastAPI** (Backend)  
- **PostgreSQL** (Database)  
- **LangChain & FAISS** (LLM-based Retrieval)  
- **Uvicorn** (Server)  

## 📜 License  
This project is licensed under the MIT License.  
