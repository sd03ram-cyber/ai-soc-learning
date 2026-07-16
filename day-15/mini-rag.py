"""
Mini RAG — retrieve top 3 relevant chunks, pass to LLM, print answer.
Requires: pip install langchain langchain-community langchain-huggingface langchain-chroma langchain-anthropic chromadb sentence-transformers
Set your API key first: export ANTHROPIC_API_KEY="your-key-here"
Run load-docs.py first so ./chroma_db exists.
"""

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

prompt = ChatPromptTemplate.from_template(
    "Answer the question using only the context below.\n\nContext:\n{context}\n\nQuestion: {question}"
)
llm = ChatAnthropic(model="claude-sonnet-4-6")
chain = prompt | llm | StrOutputParser()


def ask(question: str) -> str:
    chunks = retriever.invoke(question)
    context = "\n\n".join(c.page_content for c in chunks)
    return chain.invoke({"context": context, "question": question})


questions = [
    "What is a SIEM and why is it needed?",
    "What is Chain-of-Thought prompting and when does it help?",
    "Why do LLMs need tools like function calling?",
]

if __name__ == "__main__":
    for q in questions:
        print(f"Q: {q}")
        print(f"A: {ask(q)}")
        print("---")

    # Expected style of output for question 1:
    # A: A SIEM centralizes logs from across a network so patterns and
    #    threats can be spotted, instead of manually checking each
    #    machine's logs individually.
