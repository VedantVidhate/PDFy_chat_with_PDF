import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.memory.buffer import ConversationBufferMemory
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain 
from langchain_community.chat_models import ChatOpenAI
from htmlTemplates import css, bot_template, user_template
from langchain.llms import HuggingFaceHub

def get_pdf_text(pdfs):
    text = ''
    for pdf in pdfs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
                text += page.extract_text()
    return text

def get_text_chunks(raw_text):
    text_splitter = CharacterTextSplitter(
        separator = "\n",
        chunk_size = 1000,
        chunk_overlap = 100,
        length_function = len
    )
    chunks = text_splitter.split_text(raw_text)
    return chunks

def get_vectorstore(text_chunks,embedder):
    
    if embedder == "OpenAI":
        embeddings = OpenAIEmbeddings()
        vectorstore = FAISS.from_texts(texts=text_chunks,embedding=embeddings)
    elif embedder == "Instructor":
        embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
        vectorstore = FAISS.from_texts(texts=text_chunks,embedding=embeddings)
    return vectorstore

def get_convesation_chain(vectorstore,llm):
    if llm == "ChatOpenAI":
       llm = ChatOpenAI()
    elif llm == "HuggingFaceHub":
       llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.5, "max_length":512})

    memory = ConversationBufferMemory(memory_key = 'chat_history',return_messages=True)
    convesational_chain = ConversationalRetrievalChain.from_llm(
        llm = llm,
        retriever = vectorstore.as_retriever(),
        memory = memory
    )
    return convesational_chain

def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)

def main():
   load_dotenv()

   st.set_page_config(page_title="PDFy: Chat with you PDFs",page_icon=":books:")
   st.write(css, unsafe_allow_html=True)

   if "conversation" not in st.session_state:
       st.session_state.conversation = None
   if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

   st.header("PDFy: Chat with you PDFs :books:")
   user_question = st.text_input("Ask a question to you PDF's:")
   if user_question:
       handle_userinput(user_question)

   with st.sidebar:
       st.subheader("Your PDF's")
       pdfs = st.file_uploader("Upload your PDF's and click on 'PROCESS'",accept_multiple_files=True)
       if st.button("Process"):
          with st.spinner("Processing"):
              raw_text = get_pdf_text(pdfs)
              text_chunks = get_text_chunks(raw_text)
              vectorstore = get_vectorstore(text_chunks,embedder="Instructor")                         ## embedder: OpenAI or Instructor
              st.session_state.conversation = get_convesation_chain(vectorstore,llm="ChatOpenAI")      ## llm     : ChatOpenAI or HuggingFaceHub

    
if __name__ == "__main__":
    main()