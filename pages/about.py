import streamlit as st

def about_page():
    st.title("About LLM PDF Chat App")

    st.markdown("""
        The LLM PDF Chat App is an interactive web application designed to facilitate question-answering 
        interactions with PDF documents. Users can upload their PDF files and engage in conversation 
        by asking questions related to the content of the document.

        **How It Works:**
        1. **Upload PDF:** Users can upload their PDF files directly through the app interface.
        2. **Ask Questions:** Once the PDF is uploaded, users can type in their questions in the provided 
           text input box.
        3. **Get Answers:** The app utilizes advanced language models to search for relevant information 
           within the document and provides answers to the user's questions in real-time.

        **Underlying Technology:**
        - **Streamlit:** The user interface of the app is built using Streamlit, a popular Python library 
          for building web applications with simple and intuitive syntax.
        - **PyPDF2:** This library is used to extract text from PDF documents, enabling the app to analyze 
          and respond to user queries.
        - **OpenAI's Language Models:** The app leverages OpenAI's language models for natural language 
          processing tasks, including text embeddings and question-answering.
        - **LangChain Library:** Various components of the app, such as text splitting and embeddings, are 
          powered by the LangChain library, providing essential functionalities for processing and analyzing 
          textual data.
        - **FAISS:** The FAISS library is utilized for efficient similarity search, enabling the app to quickly 
          identify relevant sections of the document based on user queries.

        **Development Process:**
        The LLM PDF Chat App was developed by Gabriel Kelvin F., utilizing a combination of Python libraries 
        and frameworks mentioned above. The development process involved:
        - Designing the user interface using Streamlit to create an intuitive and user-friendly experience.
        - Integrating PyPDF2 for PDF text extraction and preprocessing.
        - Implementing text splitting and embeddings using the LangChain library to prepare the document for 
          question-answering tasks.
        - Leveraging OpenAI's language models for question-answering, enabling the app to provide accurate 
          and informative responses to user queries.
        - Testing and refining the app to ensure smooth functionality and robust performance.


        **Acknowledgments:**
        Special thanks to the developers and contributors of Streamlit, PyPDF2, OpenAI, LangChain, FAISS, 
        and other libraries used in this project for their invaluable work and contributions to the open-source 
        community.
    """)

# Displaying the about page when the app is executed
if __name__ == '__main__':
    about_page()
