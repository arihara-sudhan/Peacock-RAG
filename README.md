# Peacock-RAG
<img src="https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Pqc2FQ1sCDG9cjFEClm5Ow.png" width="100%"/>
Peacock-RAG is an AI-powered conversational application built with LangChain and FastAPI. This is a simple Q&A system where users can interact with the AI by asking questions, and the system provides intelligent responses derived from a context provided by the corpus.
<img src="https://miro.medium.com/v2/format:webp/1*SbdmGHAH2gURcDERcMnfxw.png" width="100%"/>
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


Associated Shares: <a href="https://www.linkedin.com/posts/arihara-sudhan_peacock-llm-rag-activity-7283640113522253825-_-5P?utm_source=social_share_sheet&utm_medium=member_desktop_web">LINKEDIN</a> | <a href="https://medium.com/@southern_boy/a-simple-rag-for-your-peacock-0f5a766db781">MEDIUM</a> | <a href="https://arihara-sudhan.github.io/blog/The-Peacock-Legend">BLOG</a>
