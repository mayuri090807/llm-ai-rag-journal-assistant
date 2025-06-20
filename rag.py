import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from huggingface_hub.inference._providers import get_provider_helper


load_dotenv()
token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

def build_vectorstore(file_path: str):
    # Load documents from your daily log text file
    loader = TextLoader(file_path)
    documents = loader.load()

    # Split into chunks (500 chars with 50 chars overlap)
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.split_documents(documents)

    # Create HuggingFace embeddings    
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Create a FAISS vector store from docs + embeddings
    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore

def ask_question(vectorstore, question: str):
    # Initialize retriever and LLM

    retriever = vectorstore.as_retriever()
    llm  = HuggingFaceEndpoint(
        repo_id="microsoft/Phi-3-mini-4k-instruct",
        temperature=0.5,
        max_new_tokens=512,
        task="text-generation",
        huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")    
    )

    # Create a RetrievalQA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    # Get answer
    result = qa_chain({"query": question})
    return result["result"], result["source_documents"]
