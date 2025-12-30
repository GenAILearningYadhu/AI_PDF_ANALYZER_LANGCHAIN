import tempfile
from langchain_ollama import OllamaLLM
from langchain_community.embeddings import OllamaEmbeddings

my_embedding = OllamaEmbeddings(
    model= "nomic-embed-text:latest"
)
my_llm= OllamaLLM(
        model="llama3:latest",
        temperature=.5
)
prompt_template = """
        You are a highly accurate assistant specialized in document analysis. 
        Your task is to answer the question using ONLY the provided PDF context.

        Question: 
        {question}

        Document Context:
        {context}

        Rules:
        - Base your answer strictly on the Document Context provided above.
        - If the information is not present in the context, respond with "I don't know."
        - Do not use outside knowledge or make up facts.
        - Maintain a professional tone and be concise.
        """

# PyPDFLoader expects a string path. However, Streamlit's st.file_uploader provides a file-like object stored in RAM, not a path.
# FIX: save the uploaded file to a temporary location on your disk first, then give that path to LangChain.
def create_tmp_file(file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(file.read())
        return tmp.name
