# 🌐 AI Automated Portfolio Generator

An **AI-powered web application** that automatically generates a **modern, responsive portfolio website** from a user's **resume (PDF)** using **LLMs and Agentic AI workflows**.

Built during my **Agentic AI Internship at Innomatics Research Labs**, this project demonstrates how AI can move beyond chatbots to perform **real actions** like code generation, file creation, and packaging.

---

## 🚀 Features

* 📄 Upload resume in **PDF format**
* 🧠 Extracts resume content automatically
* 🤖 Uses **Google Gemini (via LangChain)** to generate frontend code
* 🎨 Produces **modern, colorful, responsive** UI
* 🧩 Separates output into **HTML, CSS, and JavaScript** files
* 📦 Bundles files into a **ZIP archive** for instant download
* ⚡ End-to-end automation from resume → portfolio website

---

## 🧠 How It Works (Workflow)

1. **Resume Upload**
   User uploads a PDF resume through a **Streamlit UI**.

2. **Text Extraction**
   The resume text is extracted using **PyPDF2**.

3. **Prompt Construction**
   Extracted resume text is passed as input to an LLM with strict system instructions to:

   * Generate only frontend code
   * Follow a specific output format
   * Avoid explanations or markdown

4. **LLM Code Generation**
   **Google Gemini** generates:

   * `index.html`
   * `style.css`
   * `script.js`

5. **Post-processing & Packaging**
   The generated code is split into files and bundled into a **ZIP**.

6. **Download**
   User downloads a ready-to-deploy portfolio website.

---

## 🏗️ Tech Stack

* **Python**
* **Streamlit** – UI layer
* **LangChain** – LLM orchestration
* **Google Gemini API** – Code generation
* **PyPDF2** – PDF text extraction
* **dotenv** – Environment variable management

---

## 📁 Project Structure

```
AI-Automated-Portfolio-Generator/
│
├── app.py                 # Main Streamlit application
├── .env                   # Environment variables (not committed)
├── requirements.txt       # Project dependencies
├── index.html             # Generated (runtime)
├── style.css              # Generated (runtime)
├── script.js              # Generated (runtime)
├── portfolio.zip          # Generated output
└── README.md              # Project documentation
```

---

## 📌 Usage

1. Open the Streamlit app in your browser
2. Upload your resume in **PDF format**
3. Click **Generate Portfolio**
4. Download the generated **portfolio.zip**
5. Deploy or customize as needed

---

## 🎯 Learning Outcomes

* Agentic AI system design
* Prompt engineering with strict constraints
* Tool-calling workflows
* LLM output parsing & validation
* Real-world AI automation pipelines

---

## 📜 License

This project is for **educational and learning purposes**.

© 2023 Prakhar Dwivedi. All rights reserved.

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to fork or contribute!
