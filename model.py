from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from transformers import pipeline, BartTokenizer
import torch
from fastapi.responses import JSONResponse

app = FastAPI()

# Enable CORS for all routes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this for production to restrict origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Check if GPU is available and set device accordingly
device = 0 if torch.cuda.is_available() else -1

# Load embeddings for query handling
embedding = HuggingFaceEmbeddings()

# Initialize Facebook BART model and pipeline
tokenizer = BartTokenizer.from_pretrained("facebook/bart-large")  # Initialize the tokenizer
generator = pipeline("text2text-generation", model="facebook/bart-large", device=device)

# Load the FAISS index
print("Loading FAISS index")
new_db = FAISS.load_local("faiss_index", embedding, allow_dangerous_deserialization=True)

# Define the expected request format
class QueryModel(BaseModel):
    question: str

# Function to get response from Facebook BART without extra printing
def get_bart_response(context):
    prompt = context
    input_ids = tokenizer.encode(prompt, return_tensors='pt')
    num_tokens = input_ids.shape[1]
    max_length = min(num_tokens + 50, 1024)
    response = generator(prompt, max_length=max_length, truncation=True)
    generated_text = response[0]['generated_text'].strip()

    if "Answer:" in generated_text:
        answer_start = generated_text.index("Answer:") + len("Answer:")
        return generated_text[answer_start:].strip()
    else:
        return generated_text

# Main endpoint
@app.post("/get-response")
async def get_response(data: QueryModel):
    question = data.question

    # Perform similarity search in FAISS
    res = new_db.similarity_search(question, k=1)
    combined_context = " ".join([r.page_content for r in res])

    # Generate a response using Facebook BART
    output = get_bart_response(combined_context)
    return {"response": output}

# Optional: CORS preflight support
@app.options("/get-response")
async def options_get_response():
    return JSONResponse(status_code=200)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000)