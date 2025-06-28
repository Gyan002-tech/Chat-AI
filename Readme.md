# Chat AI: Retrieval-Augmented Conversational Assistant

## Overview

Chat AI is a web-based conversational assistant that leverages Retrieval-Augmented Generation (RAG) to provide accurate, context-aware answers. It combines a modern web UI with a FastAPI backend powered by HuggingFace LLMs, LangChain, and a Chroma vector database for document retrieval. The system is designed for extensibility and can be adapted to various document sources and prompt strategies.

## Features

- **Conversational AI**: Chat with an LLM that can use both its own knowledge and retrieved document context.
- **Retrieval-Augmented Generation**: Answers are improved by retrieving relevant information from indexed documents.
- **Prompt Engineering**: Uses custom prompt templates for both query rewriting and answer generation.
- **Memory Management**: Maintains conversation context using summary memory for more coherent multi-turn dialogs.
- **Modern Web UI**: Responsive chat interface with light/dark mode and conversation history.

## Architecture

- **Frontend**: HTML, CSS, and JavaScript provide a chat interface with conversation management and theming.
- **Backend**: FastAPI server exposes endpoints for chat, powered by HuggingFace LLMs via LangChain.
- **Vector Store**: Chroma DB stores document embeddings for fast retrieval.
- **Prompt Templates**: JSON and Python-based templates for answer and query rewriting.
- **Document Processing**: PDF documents are loaded, split, and embedded for retrieval.

## Setup & Installation

1. **Clone the repository** and install Python dependencies:
   ```bash
   pip install -r requirements.txt
   # or manually install: fastapi, uvicorn, langchain, huggingface_hub, chromadb, python-dotenv, etc.
   ```
2. **Set up environment variables** (see `.env` for API keys if needed).
3. **Prepare documents**: Place your PDFs in the appropriate directory and run the notebook or scripts to index them.
4. **Start the backend server**:
   ```bash
   python model.py
   # or
   uvicorn model:app --reload
   ```
5. **Open `index.html`** in your browser to use the chat interface.

## Usage

- Type your question in the chat box and press send.
- The assistant will answer using its own knowledge or, if needed, by retrieving relevant context from indexed documents.
- Send 'exit' to end the conversation.

## File Structure

- `index.html` / `style.css` / `script.js`: Web UI files
- `model.py`: FastAPI backend with LangChain RAG pipeline
- `pg_1.py`, `pg_2.py`: Prompt template generators (answer and query rewriting)
- `template_1.json`, `template_2.json`: JSON prompt templates
- `Model.ipynb`: Jupyter notebook for document loading, splitting, embedding, and testing
- `Chroma_db/`: Chroma vector database files
- `ugrulebook_2.pdf`: PDF document

## Technical Notes & Research

- **Text Splitting**: Uses recursive character splitting for reliable chunk sizes (semantic chunking was inconsistent).
- **Document Loaders**: PDFPlumberLoader chosen for best format preservation; other loaders tested.
- **Vector Stores**: Chroma used for local testing; Pinecone, Weaviate, Qdrant considered for production/hybrid search.
- **Retrievers**: Multi-query retriever outperformed basic similarity search but is more resource-intensive.
- **Memory**: ConversationSummaryMemory used for efficient context retention; CombinedMemory tested but found resource-heavy for long responses.

## Credits

- Built with [LangChain](https://github.com/langchain-ai/langchain), [HuggingFace](https://huggingface.co/), [Chroma](https://www.trychroma.com/), and [FastAPI](https://fastapi.tiangolo.com/).
- UI inspired by modern chat applications.

---

_For more details, see the code and comments in each file._
