# PDF to QnA System using Streamlit

This project demonstrates a simple web application that allows users to upload a PDF file, extract text from it, and then ask questions to obtain answers from the extracted text. It utilizes the Streamlit framework, PyPDF2 library for PDF text extraction, and the Hugging Face Transformers library for Question Answering.

## Getting Started

### Prerequisites

Make sure you have the following libraries installed:

- `streamlit`
- `PyPDF2`
- `transformers`

You can install them using the following command:

```bash
pip install streamlit PyPDF2 transformers

=> INSTALLATION

1. Clone this repository:
git clone https://github.com/rAvIkUmRa/Document-QnA-System.git
cd pdf-to-qna-app


2.Run the Streamlit app:
streamlit run app.py


The app should open in your web browser, allowing you to upload a PDF file, extract text, and ask questions.

=> HOW TO USE

1. Open the app in your web browser after running the streamlit run app.py command.

2. Upload a PDF file by clicking the "Upload a PDF file" button.

3. The app will display the extracted text from the PDF.

4. Enter a question in the "Ask a question:" input box.

5. The app will use a pre-trained model to provide an answer based on the extracted text and the question.

=> LICENSE
This project is licensed under the MIT License - see the LICENSE file for details.

=>ACKNOWLEDGEMENT

*This project uses the Streamlit framework (https://streamlit.io/).
*Text extraction from PDF is performed using the PyPDF2 library (https://github.com/mstamy2/PyPDF2).
*Question Answering is powered by the Hugging Face Transformers library (https://huggingface.co/transformers).