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
1. As of now there are only 22 questions so the searching for answer is quite easy and fast but as the number of questions in the database will increase this task will start to take a lot of time. To solve this problem of taking so much of time we can add metadata to the input file before the pre-processing the document and then use these metadata fields to search through the database much faster.

  Metadata fields that we have in mind:
    1. Author/Source: storing who was the author or source of the information
    2. Keywords: to search through the database based on the keywords in the User's query and in the answers stored in the database
    3. Last Updated: To keep track of document status
    4. Category: to search through different varieties of documents. let's say some body is searching for question from the Admissions category so we can find          based on the keywords and then rather than searching through the whole document we can just search only that category of document.
    5. Confidence Score: found based on the upvote the response recieves like there is a small upvote and downvote button below every response of chatgpt so we         can also utilize this technique as well.
    6. num_word: stores the number of words present in the question

2. We are thinking of adding a feature that once a user submits a query we will not only answer the query but we will also suggest 2-3 follow-up questions.
   Procedure: we will be doing this using a simple logic that rather than searching for 1 most relevant question of the query and output that which we are doing               now. We will search for 3 most relevant questions and then output the answer of 1st most relevant question along with the 2nd and 3rd most                       relevant questions that we found so that user doesn't have to think what should he do next and it will save his some time as he will not have to                 type obvious follow-up questions.

3. We are also thinking of adding an spell checker using TextBlob module.
