from app.embeddings.vector_store import vector_store
from app.rag.prompt import build_prompt
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

def query_knowledge_base(question: str, k: int = 4):
    docs = vector_store.similarity_search(
        question,
        k=k
    )

    if not docs:
        return {
            "answer": "No se dispone de información suficiente en la base de conocimiento.",
            "sources": []
        }

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = build_prompt(context, question)

    response = llm.invoke(prompt)

    sources = [
        {
            "content": doc.page_content[:300],
            "metadata": doc.metadata
        }
        for doc in docs
    ]

    return {
        "answer": response.content,
        "sources": sources
    }
