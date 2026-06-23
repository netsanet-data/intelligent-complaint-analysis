# Intelligent Complaint Analysis for Financial Services

## Project Overview

This project builds a Retrieval-Augmented Generation (RAG) chatbot for CrediTrust Financial. The chatbot helps customer support, product managers, and compliance teams quickly analyze customer complaints by retrieving relevant complaint records and generating evidence-based answers.

---

## Project Structure

```
intelligent-complaint-analysis/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── eda.ipynb
│   ├── text-chunking.ipynb
│   ├── embedding.ipynb
│   └── retriever-demo.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retriever.py
│   ├── prompt.py
│   └── generator.py
│
├── vector_store/
├── app.py
├── requirements.txt
└── README.md
```

---

## Technologies

- Python
- Pandas
- FAISS
- Sentence Transformers
- LangChain Text Splitters
- Gradio

---

## Tasks Completed

### Task 1
- Exploratory Data Analysis
- Data Cleaning
- Text Preprocessing

### Task 2
- Text Chunking
- Embedding Generation
- FAISS Vector Store

### Task 3
- Retriever
- Prompt Template
- Generator
- End-to-End RAG Pipeline

### Task 4
- Gradio Chat Interface

---

## Running the Application

```bash
python app.py
```