**AI PDF ANALYZER**

This is an interactive application built using LangChain, Streamlit, FAISS, and Ollama. The app allows users to upload a PDF file and ask questions about its content. The system retrieves relevant information from the PDF and generates accurate, context-aware answers using a locally hosted LLM.

**Key Features:**
- Upload and analyze PDF documents
- Ask natural language questions about PDF content
- Uses RAG architecture to reduce hallucinations
- Local embeddings and LLM using Ollama
- Optimized with vector store persistence and caching
- Simple and interactive Streamlit UI

**Tech Stack:**
**Python**
**LangChain**
**Streamlit**
**Ollama**
**FAISS (Vector Database)**

**Architecture (RAG Pipeline):**
1 PDF upload via Streamlit UI
2 Save uploaded PDF to a temporary file
3 Load PDF using PyPDFLoader
4 Split text into chunks using RecursiveCharacterTextSplitter
5 Generate embeddings using OllamaEmbeddings
6 Store embeddings in FAISS vector database
7 Retrieve relevant chunks using similarity search
8 Inject retrieved context into prompt
9 Generate answer using OllamaLLM
