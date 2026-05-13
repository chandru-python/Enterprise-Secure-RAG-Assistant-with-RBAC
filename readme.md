# 🚀 Enterprise Secure RAG Assistant with RBAC

<p align="center">

<img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python"/>

<img src="https://img.shields.io/badge/FastAPI-Backend-green?style=for-the-badge&logo=fastapi"/>

<img src="https://img.shields.io/badge/Streamlit-Frontend-red?style=for-the-badge&logo=streamlit"/>

<img src="https://img.shields.io/badge/LangChain-RAG-yellow?style=for-the-badge"/>

<img src="https://img.shields.io/badge/FAISS-VectorDB-purple?style=for-the-badge"/>

<img src="https://img.shields.io/badge/AI-Enterprise-black?style=for-the-badge"/>

</p>

---

# 📌 Overview

Enterprise Secure RAG Assistant is a **production-style AI-powered Retrieval-Augmented Generation (RAG) system** designed for enterprise environments.

The system retrieves accurate information from multiple disconnected enterprise data sources while enforcing strict **Role-Based Access Control (RBAC)**.

It supports:
- 🔍 Semantic Search
- 🛡️ Secure Access Control
- 📄 Multi-source Retrieval
- 🧠 Grounded AI Responses
- 📊 Explainability & Citations
- ⚡ Enterprise-grade Architecture

---

# ✨ Features

✅ Multi-format enterprise data ingestion  
✅ Semantic document retrieval using FAISS  
✅ Role-Based Access Control (RBAC)  
✅ FastAPI backend API  
✅ Streamlit frontend UI  
✅ Explainable AI responses  
✅ Source citations & traceability  
✅ Confidence score display  
✅ Audit logging system  
✅ Multi-source enterprise reasoning  
✅ Enterprise-style responsive interface  

---

# 🛠️ Technologies Used

| 🚀 Technology | 📌 Purpose |
|---|---|
| Python 3.11 | Core Programming |
| FastAPI | Backend API |
| Streamlit | Frontend UI |
| LangChain | RAG Pipeline |
| FAISS | Vector Database |
| Sentence Transformers | Embedding Model |
| Pandas | CSV Processing |
| JSON | Log Processing |
| Torch | Deep Learning Backend |

---

# 🏗️ Project Architecture

```text
                User Query
                     ↓
          Streamlit Frontend UI
                     ↓
             FastAPI Backend
                     ↓
         Authentication + RBAC
                     ↓
            LangChain Pipeline
                     ↓
            FAISS Vector Search
                     ↓
       Enterprise Dataset Sources
        (TXT / CSV / JSON Files)
                     ↓
      Grounded Response Generation
                     ↓
     Explainable AI + Citations
                     ↓
              Final Response
```

---

# 📂 Folder Structure

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

# 📊 Dataset Details

The project uses synthetic enterprise datasets consisting of:

📄 500 TXT Documents  
📈 500 CSV Records  
🧾 500 JSON Security Logs  

### 📌 Data Categories

- 🏢 HR Policies
- 💰 Finance Reports
- ⚙️ Technical Infrastructure
- 🔐 Security Logs
- 📋 Operational Records

---

# 🔐 Role-Based Access Control (RBAC)

| 👤 Role | 🔓 Access |
|---|---|
| Admin | Full Access |
| HR User | HR Documents |
| Finance User | Finance Reports |
| Technical User | Technical Documents |
| Employee | Restricted Access |

---

# ⚙️ Installation

## 📥 Clone Repository

```bash
git clone https://github.com/chandru-python/Enterprise-Secure-RAG-Assistant-with-RBAC.git

cd Enterprise-Secure-RAG-Assistant-with-RBAC
```

---

# 📦 Install Dependencies

```bash
py -3.11 -m pip install -r requirements.txt
```

---

# 🧠 Generate Vector Database

```bash
py -3.11 ingest.py
```

This will:

✅ Load enterprise datasets  
✅ Generate embeddings  
✅ Build FAISS vector database  

---

# 🚀 Run Backend

```bash
py -3.11 -m uvicorn app:app --reload
```

## 🌐 Backend URL

```text
http://127.0.0.1:8000
```

## 📑 Swagger API Docs

```text
http://127.0.0.1:8000/docs
```

---

# 💻 Run Frontend

```bash
cd frontend

py -3.11 -m streamlit run streamlit_app.py
```

## 🌐 Frontend URL

```text
http://localhost:8501
```

---

# 👨‍💻 Sample Login Credentials

| 👤 Username | 🔑 Password | 🛡️ Role |
|---|---|---|
| admin | admin123 | Admin |
| hr_user | hr123 | HR |
| finance_user | finance123 | Finance |
| technical_user | tech123 | Technical |
| employee | emp123 | Employee |

---

# 🔍 Example Queries

## 🏢 HR

```text
What is leave policy?
```

## 💰 Finance

```text
Show Q1 revenue report
```

## ⚙️ Technical

```text
What is server downtime threshold?
```

## 🔐 Security

```text
Show security logs
```

---

# 🔄 System Workflow

1️⃣ User logs into the system  
2️⃣ Query submitted through frontend  
3️⃣ RBAC validates user access  
4️⃣ FAISS retrieves relevant documents  
5️⃣ LangChain RAG pipeline processes context  
6️⃣ Grounded response generated  
7️⃣ Sources & confidence scores displayed  

---

# 🌟 Key Highlights

🚀 Enterprise-grade AI retrieval system  
🛡️ Secure document access with RBAC  
🔍 Semantic similarity search  
📄 Explainable AI responses  
📊 Source traceability & citations  
⚡ Production-style architecture  
🧠 Context-aware retrieval pipeline  

---

# 🔮 Future Enhancements

- 🤖 OpenAI GPT Integration
- 📸 OCR Document Support
- 🔑 JWT Authentication
- ⚡ Hybrid Search
- 🧠 ChromaDB Integration
- 🐳 Docker Deployment
- ☁️ Cloud Hosting
- 💬 Real-time Chat Memory

---

# 👨‍💻 Author

# Chandru

AI/ML Engineer | RAG | LLM | FastAPI | Generative AI | Computer Vision

---

# ⭐ If you like this project

Give it a ⭐ on GitHub and connect with me on LinkedIn 🚀
