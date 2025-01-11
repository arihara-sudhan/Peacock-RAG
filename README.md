# Peacock-RAG

Peacock-RAG is an AI-powered conversational application built with LangChain and FastAPI. This is a simple Q&A system where users can interact with the AI by asking questions, and the system provides intelligent responses derived from a context provided by the corpus.

## Features

- **Conversational AI**: Interact with the AI by asking questions, and get responses based on the context in the provided corpus.
- **Contextual Responses**: The AI pulls relevant information from the pre-processed and indexed text corpus to generate accurate answers.
- **Web Interface**: Simple user interface built with HTML and JavaScript to interact with the FastAPI backend.
- **FastAPI Backend**: Handles the requests and interfaces with LangChain for conversational retrieval.

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.9+
- pip (Python package installer)

### SETUP
1. Install the dependencies after cloning and creating a venv
> pip install -r requirements.txt

2. In config.py,
HUGGINGFACE_API_TOKEN: Your HuggingFace API token to use models from HuggingFace.

3. Create Vectorized Data (Embeddings 🤥)
> python3 create_vector.py
Note: corpus.txt is our data. You can use your own.

4. Run the application,
> uvicorn main:app --reload

5. Open index.html in a browser and there you go!
