# 🤖 FastAPI Chatbot API

[![Docker Pulls](https://img.shields.io/docker/pulls/ataur077/faq-bot.svg)](https://hub.docker.com/r/ataur077/faq-bot)

A lightweight and efficient chatbot API built using **FastAPI** and Dockerized for easy deployment. This project demonstrates a simple RESTful API that accepts user input and returns chatbot responses via a custom logic module.

---

## 🚀 Features

- 🔥 Fast and asynchronous REST API with FastAPI
- ♻️ CORS enabled for cross-origin communication
- 📦 Dockerized for production-ready deployment
- 🧠 Modular chatbot logic (customizable via `chatbot.py`)

---

## 📁 Project Structure
```
fastapi-chatbot/
├── app.py # Main FastAPI app
├── chatbot.py # Chat logic (stream_graph_updates function)
├── requirements.txt # Python dependencies
├── Dockerfile # Docker configuration
└── README.md # Project documentation
```

---

## 🛠️ Setup Instructions

### 🔧 Prerequisites

- Python 3.11+
- Docker

### 🐍 Run Locally (Without Docker)

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
Start the API
```
uvicorn app:app --reload
```
Visit the interactive docs:
`http://localhost:8000/docs`

### 🐳 Run with Docker (Locally)
Build the Docker image
```
docker build -t faq-bot .
```
Run the container
```
docker run -d -p 8000:8000 \
  --env GEMINI_KEY=your_real_gemini_api_key \
  ataur077/faq-bot
```

Access the API at:
`http://localhost:8000`
API Docs: `http://localhost:8000/docs`

### 🐳 Run from DockerHub (Public Image)
You can pull and run this app directly from DockerHub:
```
docker pull ataur077/faq-bot:latest
docker run -d -p 8000:8000 \
  --env GEMINI_KEY=your_real_gemini_api_key \
  ataur077/faq-bot
```
Then visit: http://localhost:8000/docs

## 📬 API Endpoints
- `GET /
Returns a status message.`
    ```
    { "message": "API is running!" }
    ```

- `POST /chat
Send user input and get chatbot response.`

    - Request Body
    ```
    {
    "user_input": "Hello, chatbot!"
    }
    ```

    - Response
    ```
    {
    "response": "Hi there! How can I help you today?"
    }
    ```

## 🧠 Customize the Chatbot
All chatbot logic is located in chatbot.py. You can define the stream_graph_updates(user_input: str) function to return responses based on any rule-based, ML-based, or LLM-based logic.

## 📄 License
This project is open-source and free to use under the [MIT License](./LICENSE.md).

