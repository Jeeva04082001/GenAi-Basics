
import streamlit as st
import pdfplumber
import os
import io
import numpy as np

from langchain_text_splitters import RecursiveCharacterTextSplitter
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

st.title("PDF RAG Chatbot")

uploaded_file = st.file_uploader(
    "Upload your PDF",
    type=["pdf"]
)


# Generate embeddings using Gemini
def create_embeddings(texts):
    result = client.models.embed_content(
        model="gemini-embedding-001",
        contents=texts,
    )

    print('result.embeddings-------------',result.embeddings)
    return [
        np.array(item.values, dtype=np.float32)
        for item in result.embeddings
    ]


# Extract text from all PDF pages
def extract_pdf(file_bytes):
    documents = []

    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        for page in pdf.pages:
            text = page.extract_text() or ""

            if text.strip():
                documents.append(text)
    print('documents:---------------------------',documents)
    return documents


# Combine all pages and split into chunks
def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
        separators=["\n\n","\n"," "]
    )

    full_text = "\n\n".join(documents)

    print(full_text[:500])

    text_chunks = splitter.split_text(full_text)
    print('text_chunks------------',text_chunks)

    chunks = []

    for text in text_chunks:
        chunks.append({
            "text": text
        })
    print('chunks:-----------------',chunks)
    return chunks


# Create an in-memory vector store
def create_vector_store(chunks):
    texts = [chunk["text"] for chunk in chunks]
    print('texts:---------------',texts)

    vectors = []
    batch_size = 50

    for start in range(0, len(texts), batch_size):
        batch = texts[start:start + batch_size]
        print(batch,'batch------------------------')
        vectors.extend(create_embeddings(batch))

    print('vectors---------------',vectors)
    return {
        "chunks": chunks,
        "vectors": vectors
    }


# Retrieve relevant chunks using cosine similarity
def retrieve_chunks(question, vector_store, k=4):
    query_vector = create_embeddings([question])[0]

    vectors = np.array(vector_store["vectors"])

    scores = vectors @ query_vector / (
        np.linalg.norm(vectors, axis=1)
        * np.linalg.norm(query_vector)
        + 1e-10
    )

    top_indices = np.argsort(scores)[::-1][:k]

    return [
        vector_store["chunks"][i]
        for i in top_indices
    ]


if uploaded_file is not None:

    file_bytes = uploaded_file.getvalue()
    print('file_bytes-------------------',file_bytes)

    # Process a new or changed PDF
    import hashlib
    file_hash = hashlib.sha256(file_bytes).hexdigest()

    print('file_hash--------------------',file_hash)
    if st.session_state.get("file_hash") != file_hash:
        try:
            with st.spinner("Processing PDF..."):

                documents = extract_pdf(file_bytes)

                if not documents:
                    st.error(
                        "No readable text found. "
                        "Scanned PDFs may need OCR."
                    )
                    st.stop()

                chunks = split_documents(documents)
                print('chunkschunkschunks-----',chunks)

                vector_store = create_vector_store(chunks)

                print('vector_storevector_storevector_store-------',vector_store)
                st.session_state.vector_store = vector_store
                st.session_state.file_hash = file_hash
                st.session_state.messages = []

            st.success(
                f"PDF processed! {len(chunks)} chunks created."
            )

        except Exception as e:
            st.error(f"PDF processing failed: {e}")
            st.stop()

    # Display chat history
    for message in st.session_state.get("messages", []):
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    question = st.chat_input("Ask something about your PDF")

    if question:
        st.session_state.messages.append({
            "role": "user",
            "content": question
        })

        with st.chat_message("user"):
            st.markdown(question)

        with st.chat_message("assistant"):
            try:
                with st.spinner("Finding the answer..."):

                    relevant_chunks = retrieve_chunks(
                        question,
                        st.session_state.vector_store
                    )

                    print('relevant_chunksrelevant_chunks----------',relevant_chunks)
                    context = "\n\n".join(
                        chunk["text"]
                        for chunk in relevant_chunks
                    )

                    response = client.models.generate_content(
                        model="gemini-2.5-flash-lite",
                        contents=f"""
                            You are a PDF question-answering assistant.

                            Answer using only the PDF context below.
                            If the answer is not present, say that the PDF
                            does not contain enough information.
                            Do not invent facts.

                            PDF context:
                            {context}

                            Question:
                            {question}
                            """,
                        config=types.GenerateContentConfig(
                            temperature=0
                        )
                    )

                    print('responseresponseresponse--------',response)
                    answer = response.text or (
                        "I could not generate an answer."
                    )

                    st.markdown(answer)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })
                
                print(st.session_state.messages,'st.session_state.messages-------')

            except Exception as e:
                st.error(f"Error: {e}")


















