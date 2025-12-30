import langchain_helper as lch
import streamlit as st
from config.streamlit_config import get_vector_db
import textwrap


# UI PART
st.title("PDF Analyzer")

with st.sidebar:
    with st.form(key="my-form"):
        uploaded_file= st.file_uploader(
            label= "Upload",
            type= "pdf"
        )

        query= st.text_area(
            label= "What is querry regarding this PDF file?",
            max_chars=100,
            key="query"
        )

        st.form_submit_button(label="Submit")



# Logic part -> calling langchain
if query and uploaded_file:
    with st.spinner("Analyzing PDF...", show_time=True):
        vector_db = get_vector_db(uploaded_file)
        response, ref_data = lch.get_response_from_db(db=vector_db, query=query)
    st.subheader("Answer:")
    st.text(textwrap.fill(response, width=80))




