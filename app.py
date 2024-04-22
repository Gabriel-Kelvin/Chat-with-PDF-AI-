import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_community.vectorstores.faiss import FAISS
from langchain.llms import OpenAI
from dotenv import load_dotenv
from langchain.chains.question_answering import load_qa_chain

# Function to display the sidebar
def display_sidebar():
    st.sidebar.title("LLM PDF Chat App")
    st.sidebar.markdown("Upload your PDF and engage in conversation!")
    add_vertical_space(0)
    st.sidebar.write("Developed by Gabriel Kelvin")

# Main function to run the application
def main():
    display_sidebar()  # Display the sidebar

    st.header("Interactive PDF Question-Answering System")
    load_dotenv()

    # Uploading PDF file
    pdf = st.file_uploader("Upload your PDF", type='pdf')

    if pdf is not None:
        # Extracting text from the PDF
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        # Splitting text into manageable chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
        )
        chunks = text_splitter.split_text(text=text)

        # Generating embeddings for the text chunks
        embeddings = OpenAIEmbeddings()
        knowledge_base = FAISS.from_texts(chunks, embedding=embeddings)

        # Getting user question input
        user_question = st.text_input("Ask your question")
        if user_question:
            # Searching for relevant documents based on user question
            docs = knowledge_base.similarity_search(user_question)

            # Initializing OpenAI language model and loading question-answering chain
            llm = OpenAI()
            chain = load_qa_chain(llm, chain_type="stuff")

            # Obtaining response from the question-answering chain
            response = chain.run(input_documents=docs, question=user_question)

            # Displaying the response
            st.write("Answer:", response)

# Running the main function if the script is executed directly
if __name__ == '__main__':
    main()

