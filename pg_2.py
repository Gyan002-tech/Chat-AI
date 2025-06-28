# Task: Prompt to Re-write Input User's Query

from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""You are a query rewriting assistant that helps improve user questions to make them clearer, more specific, and more answerable.

    Given the user question, rewrite the question to:
    - Use proper grammar and phrasing
    - Be more specific if needed
    - Align with the provided context
    - Remove any ambiguity
    - Ensure it helps retrieve or generate a better answer

    User Question: {question}
    Rewritten Query:""",
    input_variables=['question']
)

template.save("template_2.json")