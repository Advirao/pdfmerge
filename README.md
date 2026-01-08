# 📄 PDF Merger Tool – Local Usage Guide

A lightweight **Streamlit** application built with Python to merge multiple PDF files using a simple drag-and-drop web interface. The app uses a Python PDF library (such as `pypdf` / `PyPDF2`) for PDF manipulation and can use `uv` for fast dependency management in a local environment. [web:7][web:10]

---

## 🚀 Features

- **Drag & Drop** upload of multiple PDF files directly in your browser. [web:7]  
- **Fast merging** of PDFs into a single document using a Python PDF library. [web:10]  
- **Runs locally** on your machine; your PDFs never leave your system. [web:7]  

---

## 🛠️ Prerequisites

Make sure the following are installed:

- **Python 3.9+** on your local machine. [web:7]  
- **Git** (to clone the repository). [web:7]  
- **uv** (optional but recommended) for fast, isolated Python environments. [web:7]  

If you do not want to use `uv`, you can use a standard virtual environment (`venv`) and `pip` instead. [web:7]  

---

## 📥 Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/Advirao/pdfmerge.git
cd pdfmerge

 ### 2. Create and activate environment
Option A – Using uv (recommended)


uv sync

# Activate env (Linux / macOS; adjust path if needed)
source .venv/bin/activate

# On Windows (PowerShell)
# .venv\Scripts\Activate.ps1


###Option B – Using venv + pip

python -m venv .venv
source .venv/bin/activate      # On Windows: .venv\Scripts\activate

pip install streamlit pypdf
# or, if the project uses PyPDF2:
# pip install streamlit PyPDF2


### Running the Application
### From the project root (with your environment activated), run:

streamlit run app.py


After the server starts, open your browser and go to:

http://localhost:8501


Streamlit will usually open this URL automatically in your default browser.




