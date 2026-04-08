import streamlit as st
import os
import uuid
from utils import encrypter, decrypter

# ---------------- SETUP ----------------
if not os.path.exists("storage"):
    os.makedirs("storage")

st.set_page_config(page_title="Secure Document Locker", page_icon="🔐")
st.title("🔐 Secure Document Locker")

# ---------------- SESSION INIT ----------------
if "password" not in st.session_state:
    st.session_state.password = ""

if "filename" not in st.session_state:
    st.session_state.filename = ""

# ---------------- OPTION ----------------
option = st.radio("Choose Action", ["Encryption", "Decryption"])

# ---------------- FILE ----------------
uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])


if uploaded_file is None:
    st.session_state.password = ""
    st.session_state.filename = ""

# ---------------- INPUTS ----------------
password = st.text_input(
    "Enter Password",
    type="password",
    key="password"
)

file_name_input = st.text_input(
    "Enter output file name (without .pdf)",
    key="filename"
)

# ---------------- ENCRYPT ----------------
if option == "Encryption":

    if uploaded_file and password:

        if st.button("🔐 Encrypt File"):

            unique_id = str(uuid.uuid4())

            input_path = f"storage/input_{unique_id}.pdf"

            if file_name_input:
                if file_name_input.endswith(".pdf"):
                    output_name = file_name_input
                else:
                    output_name = file_name_input + ".pdf"
            else:
                output_name = f"encrypted_{unique_id}.pdf"

            output_path = f"storage/{output_name}"

            
            with open(input_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            with st.spinner("Encrypting..."):
                encrypter(input_path, output_path, password)

            st.success(f"✅ File saved as: {output_name}")

            with open(output_path, "rb") as f:
                st.download_button("📥 Download File", f, file_name=output_name)

# ---------------- DECRYPT ----------------
elif option == "Decryption":

    if uploaded_file and password:

        if st.button("🔓 Decrypt File"):

            unique_id = str(uuid.uuid4())

            input_path = f"storage/input_{unique_id}.pdf"

            if file_name_input:
                if file_name_input.endswith(".pdf"):
                    output_name = file_name_input
                else:
                    output_name = file_name_input + ".pdf"
            else:
                output_name = f"decrypted_{unique_id}.pdf"

            output_path = f"storage/{output_name}"

            with open(input_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            try:
                with st.spinner("Decrypting..."):
                    decrypter(input_path, output_path, password)

                st.success(f"✅ File saved as: {output_name}")

                with open(output_path, "rb") as f:
                    st.download_button("📥 Download File", f, file_name=output_name)

            except:
                st.error("Incorrect password or failed to decrypt")