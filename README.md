HOW TO RUN THE MODEL:

- Clone the repository
- Run the command below and log into hugging face account with your access_token
  - huggingface-cli login
- Run the command below
  python3 model.py
- If Output on running above code is "INFO APPLICATION STARTUP COMPLETE"
- Open the index.html file by double clicking
- Start Asking questions on web interface.

Note: "Response might vary depending on the computing power of the local machine or laptop "

MUST INSTALLED LIBRARY REQUIRED FOR THE WORKING OF MODEL

- Step 1: Create a requirements.txt
- Step 2: Paste all these inside the above file
  fastapi
  uvicorn[standard]
  pydantic
  langchain
  langchain-community
  transformers
  faiss-cpu
  torch
  sentence-transformers
- Step 3: run "pip install -r requirements.txt"

- Note: To run this on new dataset add the following to requirements.txt
  - nltk
  - spacy
  - re
  - sentence transformers
    <!-- Last library helps in database creation.-->
    <!-- Initial 3 for pre-processing-->

Some future modifications that we have in mind:

1. As the number of questions in the database increases, searching for answers may become slower. To address this, we can add metadata to the input files before preprocessing documents and use these metadata fields for faster database searches.

   - **Metadata fields:**
     - Author/Source
     - Keywords
     - Last Updated
     - Category
     - Confidence Score (based on upvotes)
     - num_word (number of words in the question)

2. Consider suggesting 2-3 follow-up questions after user asks a query. This can be achieved by searching for 3 most relevant questions and giving the answer of the first question as the output along with second and third most relevant questions.

3. Implement a spell checker
