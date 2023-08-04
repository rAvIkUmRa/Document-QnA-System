import streamlit as st
import PyPDF2
import tempfile
from transformers import pipeline

# Load the Question Answering model from Hugging Face Transformers
qa_model = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

def extract_text_from_pdf(pdf_file):
    text = ""
    with open(pdf_file, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

def main():
    st.title("PDF to QnA System")
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_file is not None:
        st.subheader("Extracted Text from PDF")

        # Save the uploaded file to a temporary location
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_file.write(uploaded_file.read())
        temp_file.close()

        pdf_text = extract_text_from_pdf(temp_file.name)
        st.text(pdf_text)

        c = 0
        while True:
            c+=1
            question = st.text_input("Ask a question"+str(c)+":")
            if question:
                answer = qa_model(question=question, context=pdf_text)
                st.subheader("Answer:")
                st.write(answer["answer"])
            else:
                break

if __name__ == "__main__":
    main()
