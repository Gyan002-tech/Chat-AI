## How to Run the Model

1. **Clone the repository.**
2. **Authenticate with Hugging Face:**

- Run: `huggingface-cli login`
- Log in using your Hugging Face access token.

3. **Start the application:**

- Run: `python3 model.py`
- Wait for the message: `INFO APPLICATION STARTUP COMPLETE`

4. **Open the web interface:**

- Double-click `index.html`.
- Begin asking questions via the web interface.

> **Note:** Response times may vary depending on your machine's computing power.

---

## Required Libraries

1. **Create a `requirements.txt` file.**
2. **Add the following dependencies:**

```
fastapi
uvicorn[standard]
pydantic
langchain
langchain-community
transformers
faiss-cpu
torch
sentence-transformers
```

3. **Install dependencies:**

- Run: `pip install -r requirements.txt`

**For new datasets, also add:**

- `nltk`
- `spacy`
- `re`
- `sentence-transformers`
  <!-- Last library helps in database creation.-->
  <!-- Initial 3 for pre-processing-->

---

## Planned Improvements

1. **Faster Search with Metadata:**  
   As the database grows, searching may slow down. To improve speed, add metadata to input files before preprocessing and use these fields for efficient searches.

- **Suggested metadata fields:**
  - Author/Source
  - Keywords
  - Last Updated
  - Category
  - Confidence Score (based on upvotes)
  - Number of words in the question

2. **Follow-up Question Suggestions:**  
   After a user query, suggest 2–3 related questions. Return the answer to the most relevant question, and display the next two most relevant questions as suggestions.

3. **Spell Checker:**  
   Implement a spell checker to improve user input quality.
