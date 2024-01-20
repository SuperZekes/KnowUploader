import streamlit as st
import os
import time


st.set_page_config(page_icon="📂")

# Title for the web app
st.title("Upload your file!")

# Create a file uploader widget
uploaded_file = st.file_uploader("Upload a file", type=["csv", "txt", "xlsx",'pdf', 'jar', 'py', 'pdf', 'mp3', 'docx', 'dwg', 'zip', "png", 'jpg','py','h5',"mp4"], accept_multiple_files=True)

# Check if a file has been uploaded
if uploaded_file is not None:
    strt = time.time()
    # Display the file details
    for i in uploaded_file:
        st.write("You've uploaded a file!")
        file_details = {"Filename": i.name, "Filesize": i.size}
        st.write(file_details)

        # Define a directory to save the uploaded files
        upload_dir = "uploaded_files"

        # Create the directory if it doesn't exist
        os.makedirs(upload_dir, exist_ok=True)

        # Get the file extension
        file_extension = i.name.split(".")[-1]

        unique_filename = f"{i.name}"

        # Save the uploaded file to the directory
        file_path = os.path.join(upload_dir, unique_filename)
        with open(file_path, "wb") as f:
            f.write(i.read())

        fin = time.time()
        st.success(f"File saved to: {file_path}")
        print(f"File saved to: {file_path}")
        print(f"Time was spent {fin - strt} secs ")
