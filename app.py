import gradio as gr

from src.retriever import retrieve
from src.generator import generate_answer


def chat(question):

    chunks = retrieve(question)

    answer = generate_answer(question, chunks)

    sources = "\n\n".join(chunks["chunk"].tolist())

    return answer, sources


demo = gr.Interface(
    fn=chat,
    inputs=gr.Textbox(
        lines=2,
        placeholder="Ask a question about customer complaints..."
    ),
    outputs=[
        gr.Textbox(label="Answer"),
        gr.Textbox(label="Retrieved Sources")
    ],
    title="CrediTrust Complaint Analysis Chatbot",
    description="Retrieval-Augmented Generation (RAG) chatbot for customer complaints.",
    clear_btn="Clear"
)

demo.launch(share=True)