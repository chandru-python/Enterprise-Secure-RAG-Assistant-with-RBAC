# Enterprise Secure RAG Assistant

## Overview

Enterprise Secure RAG Assistant is a production-style AI-powered Retrieval-Augmented Generation (RAG) system designed for enterprise environments.  

The system retrieves accurate information from multiple disconnected enterprise data sources while enforcing strict Role-Based Access Control (RBAC).

The application supports semantic search, grounded response generation, explainability, and secure access management across enterprise datasets.

---

# Features

- Multi-format enterprise data ingestion
- Semantic document retrieval using FAISS
- Role-Based Access Control (RBAC)
- FastAPI backend
- Streamlit frontend
- Explainable AI responses
- Source citations
- Confidence score display
- Audit logging
- Enterprise-style UI
- Multi-source reasoning

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| FastAPI | Backend API |
| Streamlit | Frontend UI |
| LangChain | RAG pipeline |
| FAISS | Vector database |
| Sentence Transformers | Text embeddings |
| Pandas | CSV processing |
| JSON | Log processing |

---

# Project Architecture

```text
User
  ↓
Streamlit Frontend
  ↓
FastAPI Backend
  ↓
Authentication + RBAC
  ↓
FAISS Vector Database
  ↓
Semantic Retrieval
  ↓
Grounded Response Generation
  ↓
Answer + Citations
```

---

# Folder Structure

```text
enterprise-rag/
│
├── app.py
├── auth.py
├── rag_pipeline.py
├── ingest.py
├── audit_logs.json
│
├── vector_store/
│   ├── index.faiss
│   └── index.pkl
│
├── datasets/
│   ├── hr/
│   ├── finance/
│   ├── logs/
│   └── technical/
│
├── frontend/
│   └── streamlit_app.py
│
├── requirements.txt
└── README.md
```

---

# Dataset Details

The project uses synthetic enterprise datasets consisting of:

- 500 TXT documents
- 500 CSV rows
- 500 JSON log records

### Data Categories

- HR policies
- Finance reports
- Technical infrastructure
- Security logs
- Operational records

---

# Role-Based Access Control

| Role | Access |
|---|---|
| Admin | All documents |
| HR User | HR documents |
| Finance User | Finance documents |
| Technical User | Technical documents |
| Employee | Restricted access |

---

# Installation

## Clone Project

```bash
git clone <repository_url>
cd enterprise-rag
```

---

# Install Dependencies

```bash
py -3.11 -m pip install fastapi
py -3.11 -m pip install uvicorn
py -3.11 -m pip install streamlit
py -3.11 -m pip install langchain==0.2.16
py -3.11 -m pip install langchain-community==0.2.16
py -3.11 -m pip install sentence-transformers==2.7.0
py -3.11 -m pip install transformers==4.41.2
py -3.11 -m pip install faiss-cpu
py -3.11 -m pip install pandas
py -3.11 -m pip install torch
```

---

# Generate Vector Database

Run:

```bash
py -3.11 ingest.py
```

This will:
- Load enterprise datasets
- Create embeddings
- Build FAISS vector database

---

# Run Backend

```bash
py -3.11 -m uvicorn app:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Swagger API Docs:

```text
http://127.0.0.1:8000/docs
```

---

# Run Frontend

```bash
cd frontend
py -3.11 -m streamlit run streamlit_app.py
```

Frontend URL:

```text
http://localhost:8501
```

---

# Sample Login Credentials

| Username | Password | Role |
|---|---|---|
| admin | admin123 | Admin |
| hr_user | hr123 | HR |
| finance_user | finance123 | Finance |
| technical_user | tech123 | Technical |
| employee | emp123 | Employee |

---

# Example Queries

## HR

```text
What is leave policy?
```

## Finance

```text
Show Q1 revenue report
```

## Technical

```text
What is server downtime threshold?
```

## Security

```text
Show security logs
```

---

# System Workflow

1. User logs into the system
2. Query is submitted
3. RBAC validates access
4. FAISS retrieves relevant documents
5. RAG pipeline generates grounded response
6. Sources and confidence scores are displayed

---

# Key Highlights

- Enterprise-grade AI retrieval system
- Secure document access
- Semantic similarity search
- Explainable AI responses
- Multi-format data support
- Production-style architecture

---

# Future Enhancements

- OpenAI GPT integration
- OCR document support
- JWT authentication
- Hybrid search
- ChromaDB integration
- Docker deployment
- Cloud hosting
- Real-time chat memory

---

# Author

Chandru

AI/ML Engineer | RAG | LLM | Computer Vision | FastAPI
