import streamlit as st
import dotenv
import langchain
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
import os
import zipfile
import PyPDF2  # Add this import for PDF text extraction

os.environ['GOOGLE_API_KEY'] = os.getenv('gemini')

st.set_page_config(page_title="Portfolio Generator", page_icon="🌐", layout="wide")

st.title("🌐 AI Automated Portfolio Generator")

# Replace text_area with file uploader
uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")

if uploaded_file is not None and st.button('Generate Portfolio'):
    # Extract text from PDF
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    resume_text = ""
    for page in pdf_reader.pages:
        resume_text += page.extract_text()
    
    # Use extracted text as prompt
    prompt = resume_text

    message = [('system','''You are an expert frontend web developer creating a stunning , professional portfolio website.

                Create HTML, CSS, and JavaScript code for a modern, visually appealing frontend website based on the user prompt. 
                Ensure the design is responsive, uses a clean color scheme (e.g., dark backgrounds with accent colors), 
                smooth animations, and professional typography. you must create an colorful and appealing website Make sections engaging with icons, gradients, and hover effects. 
                Avoid using question marks in any section headings or content.


                STRICT RULES:
                - Follow the exact format below
                - Do not add explanations
                - Do not use markdown or code fences
                - Output only code
                - at the end of the website page their should be not extra special characters and all after this © 2023 Prakhar Dwivedi. All rights reserved

                FORMAT:
                --html--
                [HTML code]
                --html--

                --css--
                [CSS code]
                --css--

                --js--
                [JavaScript code]
                --js--

                ''')]

    message.append(('user', prompt))

    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

    response = model.invoke(message)

    with open('index.html', 'w') as file:
        file.write(response.content.split('--html--')[1])

    with open('style.css', 'w') as file:
        file.write(response.content.split('--css--')[1])

    with open('script.js', 'w') as file:
        file.write(response.content.split('--js--')[1])

    with zipfile.ZipFile('portfolio.zip', 'w') as zip:
        zip.write('index.html')
        zip.write('style.css')
        zip.write('script.js')
    st.download_button('Download Portfolio', data=open('portfolio.zip', 'rb'),
                      file_name='portfolio.zip')
    st.write('success')