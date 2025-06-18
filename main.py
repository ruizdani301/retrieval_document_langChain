import os
import asyncio
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader

os.environ["OPENAI_API_KEY"] = "your-openai-api-key"
path = "texto.pdf"
loader = PyPDFLoader(path)
pages = []


async def leer_paginas():
    """
    Reads a PDF file and does semantic similarity search.
    This function reads a PDF file, convert each page into a document, and stores
    them in an in-memory vector store. Then it does a semantic similarity search
    for the query "SQS or EventBridge" and prints the most similar page with
    its content.
    """
    async for page in loader.alazy_load():
        pages.append(page)

    vector_store = InMemoryVectorStore.from_documents(pages,
                                                      GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-exp-03-07", task_type="SEMANTIC_SIMILARITY"))

    docs = vector_store.similarity_search("SQS or EventBridge", k=1)
    for doc in docs:
        print(f'Page {doc.metadata["page"]}: {doc.page_content[:300]}\n')

if __name__ == '__main__':
    asyncio.run(leer_paginas())
