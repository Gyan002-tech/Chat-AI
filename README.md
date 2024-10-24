THIS README IS ABOUT INFORMING HOW TO RUN THE MODEL:
* To run the program you have to download all the files // Or clone the repository with your local machine
* Open the index.html file through any one of your browser
* Next run the model.py code on the local machine ( using: VScode, pycharm etc)
* You can start asking your queris on the web page or the user interhface once the model.py output says "INFO APPLICATION STARTUP COMPLETE"
* Then you can ask questions on the web page " Remember- The response might vary depending on the computing power of the local machine or laptop "

LIBRARIES WHICH ARE REQUIRED FOR THE WORKING OF MODEL HAVE TO BE INSTALLED FOLLOWING ARE THE PIP INSTALL COMMANDS TO INSTALL ALL THE NECCESSARY LIBRARIES:
* Install FastAPI
pip install fastapi

* Install Uvicorn (ASGI server to run FastAPI)
pip install "uvicorn[standard]"

* Install Pydantic (for data validation models)
pip install pydantic

* Install LangChain[all] (for working with embeddings and LLMs)
pip install langchain

* Install Hugging Face Transformers (for pre-trained models)
pip install transformers

* Install FAISS (CPU version for vector search)
pip install faiss-cpu

* Install PyTorch (CPU version)
pip install torch

* one might also need to install the following libraries  nltk, spacy, re for pre-processing (required if your using this model for new dataset)
* sentence transformers library for databasing (required if your using this model for new dataset)


Some future modifications that we have in mind:

1. As the number of questions in the database increases, searching for answers may become slower. To address this, we can add metadata to the input files before preprocessing documents and use these metadata fields for faster database searches.

    * **Metadata fields:**
        * Author/Source
        * Keywords
        * Last Updated
        * Category
        * Confidence Score (based on upvotes)
        * num_word (number of words in the question)

2. Consider suggesting 2-3 follow-up questions after a user submits a query. This can be achieved by searching for 3 most relevant questions and outputting the answer to the first question along with the second and third most relevant questions.

3. Implement a spell checker using the TextBlob module.
