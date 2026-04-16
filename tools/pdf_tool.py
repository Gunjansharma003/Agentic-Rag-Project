from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings


def pdf_search(query):
    # 1. PDF load karna
    loader = PyPDFLoader("data/GenAi & Agentic Ai.pdf")
    documents = loader.load()

    # 2. Text ko chunks me todna
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    docs = text_splitter.split_documents(documents)

    # 3. Embeddings banana
    embeddings = HuggingFaceEmbeddings()

    # 4. Chroma DB me store karna
    vectorstore = Chroma.from_documents(
        docs,
        embedding=embeddings,
        persist_directory="chroma_db"
    )

    # 5. Retriever banana
    retriever = vectorstore.as_retriever()

    # 6. Query ke basis pe search
    results = retriever.get_relevant_documents(query)

    return results