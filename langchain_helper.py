from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config.langchain_config import prompt_template, create_tmp_file
from config.langchain_config import my_llm, my_embedding
import os

FAISS_DIR = "faiss_index"


def create_vector_db_from_pdf(uploaded_file) -> FAISS:
    pdf_file= create_tmp_file(uploaded_file)
    loader= PyPDFLoader(
        file_path=pdf_file,
        password=None
    )
    my_data= loader.load()

    textsplitter= RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    data_chunks= textsplitter.split_documents(my_data)

    if os.path.exists(FAISS_DIR):
        vector_db = FAISS.load_local(
            FAISS_DIR,
            my_embedding,
            allow_dangerous_deserialization=True
        )
    else:
        vector_db = FAISS.from_documents(data_chunks, my_embedding)
        vector_db.save_local(FAISS_DIR)
    return vector_db


def get_response_from_db(db, query, k=4):
    docs= db.similarity_search(query, k=k)
    context= "\n".join([doc.page_content for doc in docs])

    my_prompt= PromptTemplate(
        input_variables=["question", "context"],
        template=prompt_template
    )

    chain= my_prompt | my_llm | StrOutputParser()

    response= chain.invoke({
        "question": query,
        "context": context
    })

    return response, docs


