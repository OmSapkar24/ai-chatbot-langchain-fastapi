# 🤖 AI Chatbot with LangChain & FastAPI

[![CI/CD Pipeline](https://github.com/OmSapkar24/ai-chatbot-langchain-fastapi/actions/workflows/ci.yml/badge.svg)](https://github.com/OmSapkar24/ai-chatbot-langchain-fastapi/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)

A production-ready **FastAPI backend** with **LangChain** integration for building intelligent conversational AI applications. Features OpenAI GPT integration, conversation memory, session management, and RESTful APIs.

## ✨ Features

- 🚀 **FastAPI Framework** - High-performance async Python web framework
- 🧠 **LangChain Integration** - Powerful LLM orchestration and conversation chains
- 💬 **Conversation Memory** - Persistent chat history with session management
- 🔌 **RESTful API** - Well-structured endpoints with automatic documentation
- 🐳 **Dockerized** - Container-ready for easy deployment
- ✅ **Tested** - Comprehensive unit tests with pytest
- 🔄 **CI/CD Ready** - GitHub Actions workflow for automated testing and builds

## 🛠️ Tech Stack

- **Backend**: Python 3.11, FastAPI
- **AI/ML**: LangChain, OpenAI API
- **Testing**: pytest, pytest-asyncio
- **DevOps**: Docker, GitHub Actions
- **Code Quality**: Black, Flake8

## 📋 Prerequisites

- Python 3.11 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
- Docker (optional, for containerized deployment)

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/OmSapkar24/ai-chatbot-langchain-fastapi.git
cd ai-chatbot-langchain-fastapi
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 5. Run the Application

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## 🐳 Docker Deployment

### Build and Run with Docker

```bash
# Build the image
docker build -t ai-chatbot-langchain .

# Run the container
docker run -d -p 8000:8000 \
  -e OPENAI_API_KEY=your_api_key \
  --name chatbot-api \
  ai-chatbot-langchain
```

## 📚 API Documentation

Once running, access the interactive API documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Available Endpoints

#### `POST /chat`
Send a message and get AI response

```bash
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Hello! How can you help me?",
    "session_id": "user123"
  }'
```

**Response:**
```json
{
  "response": "Hello! I'm an AI assistant powered by LangChain...",
  "session_id": "user123",
  "timestamp": "2025-11-19T22:15:00.123456"
}
```

#### `GET /history/{session_id}`
Retrieve conversation history for a session

```bash
curl "http://localhost:8000/history/user123"
```

#### `DELETE /clear/{session_id}`
Clear conversation history for a session

```bash
curl -X DELETE "http://localhost:8000/clear/user123"
```

#### `GET /health`
Health check endpoint

```bash
curl "http://localhost:8000/health"
```

## 🧪 Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=. --cov-report=html

# Run specific test file
pytest tests/test_main.py
```

## 🏗️ Project Structure

```
ai-chatbot-langchain-fastapi/
├── main.py                 # FastAPI application and routes
├── requirements.txt        # Python dependencies
├── Dockerfile             # Docker configuration
├── .gitignore            # Git ignore rules
├── LICENSE               # MIT License
├── README.md             # This file
├── .github/
│   └── workflows/
│       └── ci.yml        # GitHub Actions CI/CD pipeline
└── tests/
    └── test_main.py      # Unit tests
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|----------|
| `OPENAI_API_KEY` | OpenAI API key for LLM access | Yes | None |
| `ENVIRONMENT` | Application environment | No | `development` |

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [FastAPI](https://fastapi.tiangolo.com/)
- Powered by [LangChain](https://python.langchain.com/)
- AI capabilities from [OpenAI](https://openai.com/)

## 📧 Contact

**Om Sapkar**  
GitHub: [@OmSapkar24](https://github.com/OmSapkar24)  
Email: omsapkar17@gmail.com

---

⭐ If you find this project useful, please consider giving it a star!
