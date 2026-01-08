
```markdown
# 📄 PDF Merger Tool – Local Usage Guide

A lightweight **Streamlit** application built with Python to merge multiple PDF files using a simple drag-and-drop web interface. The app uses a Python PDF library (such as `pypdf` / `PyPDF2`) for PDF manipulation and can use `uv` for fast dependency management in a local environment. 10]

---

## 🚀 Features

- **Drag & Drop** upload of multiple PDF files directly in your browser. 
- **Fast merging** of PDFs into a single document using a Python PDF library.
- **Runs locally** on your machine; your PDFs never leave your system.

---

## 🛠️ Prerequisites

Make sure the following are installed:

- **Python 3.9+** on your local machine. 
- **Git** (to clone the repository).
- **uv** (optional but recommended) for fast, isolated Python environments. 

If you do not want to use `uv`, you can use a standard virtual environment (`venv`) and `pip` instead. 

---

## 📥 Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/Advirao/pdfmerge.git
cd pdfmerge
```



### 2. Create and activate environment

#### Option A – Using uv (recommended)

```bash
uv sync

# Activate env (Linux / macOS; adjust path if needed)
source .venv/bin/activate

# On Windows (PowerShell)
# .venv\Scripts\Activate.ps1
```



#### Option B – Using venv + pip

```bash
python -m venv .venv
source .venv/bin/activate      # On Windows: .venv\Scripts\activate

pip install streamlit pypdf
# or, if the project uses PyPDF2:
# pip install streamlit PyPDF2
```



---

## ▶️ Running the Application

From the project root (with your environment activated), run:

```bash
streamlit run app.py
```



After the server starts, open your browser and go to:

```text
http://localhost:8501
```

Streamlit will usually open this URL automatically in your default browser.

---

## 📚 How to Use the PDF Merger

Once the Streamlit app is running:

1. **Upload PDFs**  
   - Use the drag-and-drop area or file picker labeled something like “Choose PDF files” or “Upload PDF files”.  
   - Select **two or more** PDF files you want to merge. 

2. **Check / reorder files (if supported)**  
   - If the UI shows a list of files, verify that all required PDFs are present.  
   - If the app includes ordering controls (arrows or drag-and-drop), arrange the files in the sequence you want them to appear in the merged PDF. 

3. **Start merging**  
   - Click the button labeled e.g. **“Merge PDFs”** or similar.  
   - The backend uses a merger class from `pypdf` / `PyPDF2` to append pages from each uploaded file into a single PDF.

4. **Download merged file**  
   - After processing, a **Download** button will appear (e.g. “Download merged PDF”).  
   - Click it to save the generated merged document (often named `merged.pdf`) to your local machine. 

---

## 🔧 Notes & Tips

- If you encounter issues with dependencies, re-run installation using `uv sync` or `pip install -r requirements.txt` (if such a file exists in the project). 
- Very large PDFs may take longer to merge depending on your machine’s resources. 
```


Sources
[1] pdfmerge https://github.com/Advirao/pdfmerge
