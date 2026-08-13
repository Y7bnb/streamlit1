import chromadb
import streamlit as st
from groq import Groq
from pypdf import PdfReader

msgtollm = "Give me an answer based on the given information"

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "user", "content": msgtollm}]

# # when loading env files locally
# import os
# from dotenv import load_dotenv
# load_dotenv()
# API_KEY = os.getenv("GROQ_API_KEY")

#when loading the api key from streamlit secrets
API_KEY = st.secrets["GROQ_API_KEY"]

groq_client = Groq(api_key=API_KEY)
MODEL = "llama-3.1-8b-instant"

st.logo(image="https://i.ytimg.com/vi/XAIkWgrC6o0/sddefault.jpg", size="large",
        link="https://www.youtube.com/watch?v=9PGspaFVpec&list=RD9PGspaFVpec&start_radio=1")

st.title(":rainbow[File RAG system]")

file_type = st.selectbox("Choose a file type", ["txt", "pdf", "py"])

if file_type == "txt":
    files = st.file_uploader("Upload a .txt file", type="txt", accept_multiple_files=True)
elif file_type == "pdf":
    files = st.file_uploader("Upload a .pdf file", type="pdf", accept_multiple_files=True)
elif file_type == "py":
    files = st.file_uploader("Upload a .py file", type="py", accept_multiple_files=True)
# if files and st.button("Process File"):
if files:
    chroma_client = chromadb.Client()

    try:
        chroma_client.delete_collection("documents")
    except Exception:
        pass

    collection = chroma_client.create_collection("documents")

    chunks = []
    tags = []

    chunk_size = 300
    overlap = 200
    step = chunk_size - overlap

    for file in files:
        if file_type == "txt" or file_type == "py":
            text = file.read().decode("utf-8")
        elif file_type == "pdf":
            reader = PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"

        st.write(f"File Processed: {file.name}")

        for i in range(0, len(text), step):
            chunks.append(text[i:i + chunk_size])
            tags.append(file.name + str(i))

    # st.write(tags)
    # st.write(len(chunks))

    collection.add(documents=chunks, ids=tags)

    st.session_state.collection = collection

    # Clear previous search state
    st.session_state.pop("context", None)
    st.session_state.pop("question", None)

    st.write(f"{len(chunks)} chunks added to knowledge base")
result_num = st.slider("Choose number of chunk results", min_value=1, max_value=15, value=5)
question = st.chat_input("Ask a question about the file")

if question:
    st.write("Thinking...")

    collection = st.session_state.collection
    result = collection.query(query_texts=question, n_results=result_num)

    # st.write(result["distances"])

    ids = result["ids"][0]

    st.session_state.context = result["documents"][0] + ids

    st.session_state.question = question

#     for ans in st.session_state.context:
#         st.write(ans)
#
# if st.button("LLM answer"):
    st.write("contacting LLM...")

    context = "\n".join(st.session_state.context)
    question = st.session_state.question

    messages = [
        {"role": "system", "content": "Answer the user's question using only the provided document context. If the context contains enough information to answer, give the answer."},
        {"role": "user", "content": f"DOCUMENT CONTEXT:\n{context}\n\nQUESTION:\n{question}"}
    ]

    response = groq_client.chat.completions.create(model=MODEL, messages=messages)
    st.write("LLM Answer:", response.choices[0].message.content)
