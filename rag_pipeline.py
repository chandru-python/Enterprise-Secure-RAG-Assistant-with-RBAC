import json
from datetime import datetime

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# ============================================
# LOAD EMBEDDING MODEL
# ============================================

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ============================================
# LOAD VECTOR DATABASE
# ============================================

vectorstore = FAISS.load_local(
    "vector_store",
    embedding_model,
    allow_dangerous_deserialization=True
)

# ============================================
# ROLE ACCESS CONTROL
# ============================================

def role_allowed(user_role, doc_department):

    # ADMIN CAN ACCESS EVERYTHING
    if user_role == "admin":
        return True

    # EMPLOYEE ONLY GENERAL ACCESS
    if user_role == "employee":
        return False

    return user_role == doc_department

# ============================================
# AUDIT LOGGING
# ============================================

def log_query(username, query):

    log = {
        "user": username,
        "query": query,
        "timestamp": str(datetime.now())
    }

    try:

        with open(
            "audit_logs.json",
            "r"
        ) as f:

            logs = json.load(f)

    except:

        logs = []

    logs.append(log)

    with open(
        "audit_logs.json",
        "w"
    ) as f:

        json.dump(logs, f, indent=4)

# ============================================
# RETRIEVE ANSWER
# ============================================

def retrieve_answer(query, role, username):

    # SAVE QUERY LOG
    log_query(username, query)

    # SEARCH VECTOR DB
    docs = vectorstore.similarity_search_with_score(
        query,
        k=5
    )

    authorized_docs = []

    # CHECK RBAC
    for doc, score in docs:

        department = doc.metadata["department"]

        if role_allowed(role, department):

            authorized_docs.append(
                (doc, score)
            )

    # NO ACCESS
    if len(authorized_docs) == 0:

        return {
            "answer": "No authorized documents found.",
            "sources": []
        }

    # BUILD CONTEXT
    context = "\n\n".join([

        doc.page_content

        for doc, score in authorized_docs
    ])

    # GROUNDED RESPONSE
    answer = f"""
Based on authorized enterprise documents:

{context[:1200]}
"""

    # SOURCE CITATIONS
    sources = []

    for doc, score in authorized_docs:

        sources.append({
            "source": doc.metadata["source"],
            "department": doc.metadata["department"],
            "confidence_score": round(float(score), 2)
        })

    return {
        "answer": answer,
        "sources": sources
    }
