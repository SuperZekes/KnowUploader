import os
import streamlit as st
from pathlib import Path

uploaded_files_dir = 'uploaded_files'

st.set_page_config(page_title="KnowUploader | Files", page_icon="📂") 

st.header('Files')

if not os.path.exists(uploaded_files_dir):
    st.write("You have not uploaded any files yet!")
else:
    files = os.listdir(uploaded_files_dir)

    for file in files:
        file_path = os.path.join(uploaded_files_dir,file)
        with open(file_path,"rb") as f:
            btn = st.download_button(
                label=""+file,
                data=f,
                file_name=file,
                mime="application/octet-stream"
            )
