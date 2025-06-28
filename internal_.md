# RAG Pipeline Component Analysis and Decisions

This document outlines the evaluation process and decisions made for key components of the Retrieval-Augmented Generation (RAG) pipeline.

---

## 1. Text Splitting

### Methods Explored

- Semantic Chunking
- Recursive Text Splitting

### Analysis and Decision

The initial approach using semantic chunking yielded inconsistent results. While some chunks were appropriately sized at 300–400 words, others spanned entire pages. This variance is detrimental to vector embedding, as overly large and dense chunks can dilute semantic granularity and harm retrieval performance.

Consequently, **Recursive Text Splitting** was chosen for its reliability and control over chunk size.

> **Next Step:** Experiment with the `chunk_overlap` parameter to improve context continuity between chunks.

---

## 2. Document Loaders

### Methods Explored

- `PyMuPDFLoader` / `PyPDFLoader`
- `UnstructuredPDFLoader`
- `PDFPlumberLoader`

### Analysis and Decision

- **`PyMuPDFLoader` / `PyPDFLoader`**: These loaders are suitable for simple, text-based PDFs but struggle with documents that have complex layouts or heavy formatting.
- **`UnstructuredPDFLoader`**: Although designed to handle complex formats, this loader parsed content at the character level in our tests. This broke structured headers (e.g., "4.1: Senate Meeting" became "4.1", ":", "Senate Meeting"), severely degrading coherence.
- **`PDFPlumberLoader`**: This loader was ultimately selected due to its superior reliability in preserving document structure. Its performance aligned with broader community feedback and produced the cleanest, most coherent output during evaluation.

**Final Choice**: `PDFPlumberLoader`

---

## 3. Vector Stores

### Methods Explored

- **Chroma** (currently in use): A lightweight and fast vector store, ideal for local experimentation and rapid prototyping.
- **Pinecone**: A cloud-native, production-ready solution that offers advanced features like hybrid search (dense + sparse retrieval).
- **Weaviate**: A powerful store that supports multi-modal data and hybrid search, making it a strong choice for media-rich datasets.
- **Qdrant**: An open-source, scalable alternative that provides all the core features found in Pinecone. It is highly recommended for customizable deployments.
- **Faiss**: Not considered optimal for RAG scenarios due to its lack of metadata filtering, a feature essential for many advanced retrieval workflows.

### Status

Currently using `Chroma` for development, with `Qdrant` and `Pinecone` as the leading candidates for production.

---

## 4. Retrievers

### Methods Explored

- `similarity_search`
- `mmr` (Maximal Marginal Relevance)
- `multi_query_retriever`
- `hybrid_search`

### Analysis and Decision

- **`similarity_search`**: Performed poorly in manual testing, frequently failing to capture contextual relevance in its answers.
- **`mmr`**: Gave results that were not a notable improvement over basic similarity search.
- **`multi_query_retriever`**: Provided substantially better results, successfully addressing nuanced queries where other methods failed. The primary downsides are increased latency and higher compute requirements.
- **`hybrid_search`**: Showed the most promise, especially in setups supported by vector stores like Pinecone or Weaviate. It effectively balances lexical (keyword) and semantic matching.

**Conclusion**: `multi_query_retriever` offers immediate quality gains, while `hybrid_search` is the target for a mature, production-level system.

---

## 5. Memory Management

### Methods Explored

- `ConversationBufferMemory`: Stores the full chat history, but quickly becomes bulky and inefficient.
- `ConversationBufferWindowMemory`: Limits memory to the last `k` exchanges. An improvement, but still inadequate for maintaining long-range context.
- `ConversationSummaryMemory`: Summarizes past exchanges, providing a good balance between performance and resource consumption.
- `ConversationKGMemory`: Best suited for knowledge-dense dialogues (e.g., technical, medical) and relies heavily on accurate Named Entity Recognition (NER).
- `CombinedMemory`: Combines short-term window memory with long-term summaries. However, initial testing revealed it to be resource-intensive, causing memory spikes when generating large responses.

### Analysis and Decision

While `CombinedMemory` is theoretically strong, its practical implementation proved too resource-heavy for our use case. `ConversationSummaryMemory` performed reliably and efficiently across tests.

**Final Choice**: `ConversationSummaryMemory` was selected for its balanced and consistent performance.
