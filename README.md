**AI PDF Analyzer**

An interactive application built using LangChain, Streamlit, FAISS, and Ollama. This tool allows users to upload PDF documents and engage in natural language conversations with their data. The system generates accurate, context-aware answers by leveraging a locally hosted Large Language Model (LLM) through a RAG pipeline.

**Key Features:**
1. PDF Analysis: Seamlessly upload and process complex PDF documents.
2. Natural Language Querying: Ask questions in plain English and get precise answers.
3. RAG Architecture: Reduces hallucinations by grounding responses in the provided document context.
4. Privacy-Focused: Uses Ollama for local embeddings and LLM execution—no data leaves your machine.
5. Optimized Performance: Features vector store persistence and Streamlit caching for faster response times.
6. User-Friendly UI: Simple, intuitive interface built with Streamlit.

**Tech Stack:**
- Language: Python
- Orchestration: LangChain
- Frontend: Streamlit
- Local LLM/Embeddings: Ollama
- Vector Database: FAISS

**Architecture (RAG Pipeline):**
- The application follows a standard Retrieval-Augmented Generation (RAG) workflow to ensure accuracy:
- PDF Upload: User uploads a file via the Streamlit UI.
- Temporary Storage: The file is saved to a temporary path for processing.
- Document Loading: PyPDFLoader extracts text from the PDF.
- Text Splitting: Text is divided into smaller, overlapping chunks using RecursiveCharacterTextSplitter.
- Embedding Generation: OllamaEmbeddings converts text chunks into high-dimensional vectors.
- Vector Storage: Embeddings are indexed in a FAISS database.
- Retrieval: The system performs a Similarity Search to find the most relevant chunks for a user's query.
- Prompt Injection: Retrieved context is combined with the user's question.
- Generation: OllamaLLM produces the final answer based strictly on the context.

**Getting Started:**
Clone the repository:

Bash

git clone https://github.com/yourusername/AI_PDF_Analyzer_Langchain.git
cd AI_PDF_Analyzer_Langchain

Install dependencies:

Bash

pip install -r requirements.txt

Run the app:

Bash

streamlit run main.py
