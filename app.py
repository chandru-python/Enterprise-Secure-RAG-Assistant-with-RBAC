from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from auth import authenticate
from rag_pipeline import retrieve_answer

# =====================================================
# FASTAPI APPLICATION
# =====================================================

app = FastAPI(
    title="Enterprise Secure RAG API",
    description="""
    Enterprise-grade Retrieval-Augmented Generation (RAG) API
    with Role-Based Access Control (RBAC),
    FAISS Vector Search,
    and Explainable Responses.
    """,
    version="1.0.0"
)

# =====================================================
# ENABLE CORS
# =====================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =====================================================
# REQUEST MODEL
# =====================================================

class QueryRequest(BaseModel):

    username: str
    password: str
    query: str

# =====================================================
# ROOT ENDPOINT
# =====================================================

@app.get("/")

def home():

    return {
        "message": "Enterprise Secure RAG API Running Successfully",
        "status": "active",
        "version": "1.0.0"
    }

# =====================================================
# MAIN RAG ENDPOINT
# =====================================================

@app.post("/ask")

def ask_question(request: QueryRequest):

    try:

        # =============================================
        # AUTHENTICATION
        # =============================================

        role = authenticate(
            request.username,
            request.password
        )

        # INVALID USER
        if not role:

            return {
                "success": False,
                "error": "Invalid username or password"
            }

        # =============================================
        # RETRIEVE ANSWER
        # =============================================

        response = retrieve_answer(
            request.query,
            role,
            request.username
        )

        return {
            "success": True,
            "user": request.username,
            "role": role,
            "query": request.query,
            "answer": response["answer"],
            "sources": response["sources"]
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }
