# Document Question Answering System

A backend system built with **Django + LangChain + HuggingFace** that allows users to ask questions based on stored documents.

This project implements a complete **Retrieval-Augmented Generation (RAG)** pipeline from scratch, including document management, TF-IDF retrieval, and LLM-based answer generation.

---

## Project Overview

This system allows:

-  Managing documents via Django Admin
-  Retrieving relevant documents using TF-IDF + Cosine Similarity
-  Generating answers using a free LLM (google/flan-t5-base)
-  Storing questions and answers in the database
-  Running the whole system with Docker

The architecture follows a clean **service-based structure** and a proper RAG workflow.

---

##  Project Structure

```
LLMProject_Roshan/
├── Dockerfile
├── docker-compose.yml
├── manage.py
├── requirements.txt
├── db.sqlite3
└── roshan_internship/
    ├── settings.py
    ├── urls.py
    ├── wsgi.py
    ├── asgi.py
    └── qa/
        ├── models.py
        ├── admin.py
        ├── views.py
        ├── urls.py
        ├── migrations/
        └── services/
            ├── retriever.py     
            ├── llm.py           
            └── qa_pipeline.py   
```

---

##  Technologies Used

- Python
- Django
- LangChain
- HuggingFace Hub
- scikit-learn
- Docker

---

##  Installation & Run

### Clone the repository

```bash
git clone https://github.com/your-username/LLMProject_Roshan.git
cd LLMProject_Roshan
```

###  Create `.env` file

Create a `.env` file in the project root:

```
HUGGINGFACEHUB_API_TOKEN=your_token_here
```

### Run with Docker

```bash
docker compose up --build
```

Then visit:

```
http://localhost:8000/admin
```

---

##  API Usage

### Endpoint

```
POST /qa/ask/
```

### Request Body

```json
{
  "question": "Your question here"
}
```

### Response

```json
{
  "question": "Your question here",
  "answer": "Generated answer based on relevant documents."
}
```

---

##  Database Models

### Document
- title
- content
- created_at
- tags

### Question
- question_text
- answer_text
- created_at

---

##  Example Flow

1. Admin uploads 3 documents.
2. User sends a question via API.
3. System retrieves top 3 relevant documents.
4. LangChain builds structured prompt.
5. flan-t5-base generates answer.
6. Answer is saved and returned as JSON.

---

##  Possible Improvements

- Add caching for repeated questions
- Replace TF-IDF with embeddings
- Add Swagger API documentation
- Add question history endpoint
- Add automated tests

