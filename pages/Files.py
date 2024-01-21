import os
import streamlit as st
from pathlib import Path

uploaded_files_dir = 'uploaded_files' 

st.header('Files')

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
