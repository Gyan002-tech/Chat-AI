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
