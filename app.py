
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Study Assistant")

class ChatRequest(BaseModel):
    message: str

def get_response(message: str) -> str:
    text = message.lower().strip()

    if not text:
        return "Please enter a question."

    if any(word in text for word in ["hello", "hi", "halo", "hey"]):
        return "Hello! I am Study Assistant. Ask me about Python, SQL, or Docker."

    if "python" in text:
        return (
            "Python is a programming language. "
            "It is widely used for data analysis, automation, and AI. "
            "Example: print('Hello World')"
        )

    if "sql" in text or "select" in text or "database" in text:
        return (
            "SQL is used to manage and query relational databases. "
            "Example: SELECT * FROM students;"
        )

    if "docker" in text or "container" in text:
        return (
            "Docker packages an application and its dependencies "
            "into a container so it can run in different environments."
        )

    if "fastapi" in text or "api" in text:
        return (
            "FastAPI is a Python framework for building APIs. "
            "You can test this app at /docs."
        )

    return (
        "Sorry, I can only answer questions about Python, SQL, "
        "Docker, and FastAPI. Please ask a question within this scope."
    )

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/chat")
def chat(request: ChatRequest):
    answer = get_response(request.message)
    return {
        "question": request.message,
        "answer": answer
    }
