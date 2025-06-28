# Task: Final Prompt with {Context} + {Re-Written User Query}

from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""
You are a helpful assistant.

First, try to answer the user's question using your own knowledge.

If the question requires specific information and you cannot answer confidently, then refer to the context provided below.

**Context (retrieved from documents):**
{context}

**Question:**
{question}

**Instructions:**
- If you know the answer from your own knowledge, answer directly.
- If not, use the context to try to answer.
- If you still don't know the answer, respond with: "Don't know".
- Do not copy from the context verbatim — paraphrase and explain clearly.

**Answer:**""",
    input_variables=["context", "question"],
    validate_template=True
)

template.save("template_1.json")