# Free Study Assistant Chatbot

A simple, free, and lightweight study assistant chatbot built with Python and FastAPI. This project uses TF-IDF and cosine similarity to match users' questions with answers from a local knowledge base.

The application is containerized using Docker and can be shared through Docker Hub, making it easier to run in different environments.

## Features

- **Question and Answer:** Answers basic questions about Python, SQL, Docker, APIs, and Machine Learning.
- **Text Similarity:** Uses TF-IDF and cosine similarity to identify the most relevant question in the knowledge base.
- **REST API:** Built with FastAPI to handle user questions and return answers.
- **API Documentation:** Provides interactive API documentation through Swagger UI.
- **Docker Support:** Packages the application and its dependencies into a Docker image.
- **Free to Use:** Does not require a paid API, API key, or cloud AI service.

## Technologies Used

- Python
- FastAPI
- Scikit-learn
- Uvicorn
- Docker
- Git and GitHub

## How It Works

1. The user submits a question through the API.
2. The application converts the question into numerical features using TF-IDF.
3. Cosine similarity compares the submitted question with questions in the local knowledge base.
4. The application returns the answer associated with the most similar question.
5. If the question does not match the supported topics sufficiently, the application returns a fallback response.

**Note:** This is a retrieval-based chatbot, not a generative AI chatbot. It selects answers from predefined knowledge and does not generate new answers like ChatGPT.

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/aldrichch/study-assistant.git
cd study-assistant
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
uvicorn app:app --reload
```

### 4. Open the API Documentation

Visit the following URL in your browser:

http://localhost:8000/docs

You can test the `/chat` endpoint directly through the interactive Swagger UI.

## Run with Docker

Build the Docker image:

```bash
docker build -t study-assistant:1.0 .
```

Run the container:

```bash
docker run -d --name study-assistant-container -p 8000:8000 study-assistant:1.0
```

Open the API documentation:

http://localhost:8000/docs

To stop the container:

```bash
docker stop study-assistant-container
```

## Example Request

Send a POST request to `/chat` with a JSON body like this:

```json
{
  "message": "What is Python?"
}
```

The exact response format depends on the application's implementation.

---

This project is intended for educational purposes and demonstrates a simple approach to building and containerizing a retrieval-based chatbot.
