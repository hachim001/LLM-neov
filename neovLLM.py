import os
import streamlit as st
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.prompts import ChatPromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq

# Définition des clés API directement dans le script
groq_api_token = "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"
huggingface_api_token = "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"

st.set_page_config(page_title="Chat Neov", page_icon=":speech_balloon:", layout="wide")
st.title("📂 Chat Neov")
st.write("Téléchargez des fichiers PDF et TXT.")

if not huggingface_api_token or not groq_api_token:
    st.error("Les clés API ne sont pas définies.")
    st.stop()

embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
language_model = ChatGroq(groq_api_key=groq_api_token, model_name="Gemma2-9b-It")

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📤 Téléchargement de fichiers")
    uploaded_files = st.file_uploader("Choisissez des fichiers (PDF ou TXT)", type=["pdf", "txt"], accept_multiple_files=True)

    documents = []
    if uploaded_files:
        for uploaded_file in uploaded_files:
            if uploaded_file.size == 0:
                st.warning(f"Le fichier {uploaded_file.name} est vide et ne sera pas traité.")
                continue
            file_extension = os.path.splitext(uploaded_file.name)[1].lower()

            temp_path = f"./{uploaded_file.name}"
            with open(temp_path, "wb") as file:
                file.write(uploaded_file.getvalue())
            
            document_loader = PyPDFLoader(temp_path) if file_extension == ".pdf" else TextLoader(temp_path)
            loaded_documents = document_loader.load()
            
            if loaded_documents:
                documents.extend(loaded_documents)
            else:
                st.warning(f"Le fichier {uploaded_file.name} ne contient aucun contenu utilisable.")

    if documents:
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=5000, chunk_overlap=200)
        text_chunks = text_splitter.split_documents(documents)

        if text_chunks:
            vector_store = Chroma.from_documents(documents=text_chunks, embedding=embedding_model, persist_directory="./chroma_db")
            retriever = vector_store.as_retriever()

            system_prompt = """
            Vous êtes un assistant intelligent. Répondez aux questions en vous basant sur le contexte fourni.
            Si la réponse n'est pas disponible, dites que vous ne savez pas.
            {context}
            """
            qa_prompt = ChatPromptTemplate.from_messages([("system", system_prompt), ("human", "{input}")])
            question_answer_chain = create_stuff_documents_chain(language_model, qa_prompt)
            retrieval_augmented_generation_chain = create_retrieval_chain(retriever, question_answer_chain)

            st.session_state.chat_chain = retrieval_augmented_generation_chain

with col2:
    st.subheader("💬 Chatbot")
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    user_input = st.chat_input("Posez votre question :")
    if user_input and "chat_chain" in st.session_state:
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        assistant_response = st.session_state.chat_chain.invoke({"input": user_input})
        assistant_message = assistant_response["answer"]

        st.session_state.messages.append({"role": "assistant", "content": assistant_message})
        with st.chat_message("assistant"):
            st.markdown(assistant_message)