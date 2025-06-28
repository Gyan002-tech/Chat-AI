from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import JSONResponse

from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint, HuggingFaceEndpointEmbeddings
from langchain.vectorstores import Chroma
from langchain_core.prompts import load_prompt, PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnableLambda, RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
from langchain.retrievers.contextual_compression import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain.chains import ConversationChain
from langchain.memory import ConversationSummaryMemory

# Load environment variables
load_dotenv()

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Initialization ---

# LLM
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation",
    temperature=0.5
)
model = ChatHuggingFace(llm=llm)

# Embedding Model
embed_model = HuggingFaceEndpointEmbeddings(client="Qwen/Qwen3-Embedding-8B")

# Chroma DB
vector_store = Chroma(
    embedding_function=embed_model,
    persist_directory="Chroma_db",
    collection_name="my_sample"
)

# Contextual Compression Retriever
base_retriever = vector_store.as_retriever(search_kwargs={"k": 10})
compressor = LLMChainExtractor.from_llm(llm=model)
compression_retriever = ContextualCompressionRetriever(
    base_retriever=base_retriever,
    base_compressor=compressor
)

# Prompts
final_prompt = load_prompt(path="template_1.json")
pre_prompt = load_prompt(path="template_2.json")
parser = StrOutputParser()

def format_docs(retrieved_docs):
    return "\n\n".join(doc.page_content for doc in retrieved_docs)

# Chain
parallel_chain = RunnableParallel({
    'context': pre_prompt | model | parser | compression_retriever | RunnableLambda(format_docs),
    'question': RunnablePassthrough()
})

qa_chain = parallel_chain | final_prompt | model | parser

# Memory
summary_memory = ConversationSummaryMemory(
    llm=model,
    return_messages=True
)

conversation = ConversationChain(
    llm=model,
    memory=summary_memory,
    verbose=True
)

# API Models
class QueryModel(BaseModel):
    question: str

# Endpoint
@app.post("/get-response")
async def get_response(data: QueryModel):
    user_input = data.question
    response = conversation.predict(input=user_input)
    return {"response": response}

@app.options("/get-response")
async def options_get_response():
    return JSONResponse(status_code=200)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000)