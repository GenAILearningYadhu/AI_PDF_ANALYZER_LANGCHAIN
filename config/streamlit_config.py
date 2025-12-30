import streamlit as st
import langchain_helper as lch


# Create a cached function so it doesn't repeat the work
@st.cache_resource
def get_vector_db(file):
    # This only runs once per file upload
    return lch.create_vector_db_from_pdf(uploaded_file=file)


