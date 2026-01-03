import streamlit as st
from pypdf import PdfWriter
import io

st.set_page_config(page_title="PDF Drag & Drop Merger", page_icon="📄")

st.title("📄 PDF Drag & Drop Merger")
st.write("Upload or drag multiple PDF files below to combine them.")

# 1. File Uploader (The Drag & Drop Zone)
uploaded_files = st.file_uploader(
    "Choose PDF files", 
    type="pdf", 
    accept_multiple_files=True
)

if uploaded_files:
    st.write(f"📂 **Files ready to merge:** {len(uploaded_files)}")
    
    # Optional: Let user see the order
    file_names = [file.name for file in uploaded_files]
    st.info("Files will be merged in this order: " + " ➡️ ".join(file_names))

    # 2. Output Filename
    output_name = st.text_input("Final Filename:", value="merged_document.pdf")

    # 3. Merge Logic
    if st.button("Merge & Download", type="primary"):
        merger = PdfWriter()
        
        try:
            for uploaded_file in uploaded_files:
                # Read the file directly from memory
                merger.append(uploaded_file)
            
            # Create an in-memory buffer for the result
            output_pdf = io.BytesIO()
            merger.write(output_pdf)
            merger.close()
            
            # 4. Provide Download Button
            st.success("✅ Merge Complete!")
            st.download_button(
                label="📥 Download Merged PDF",
                data=output_pdf.getvalue(),
                file_name=output_name,
                mime="application/pdf"
            )
            
        except Exception as e:
            st.error(f"An error occurred: {e}")

else:
    st.info("Waiting for files... You can select multiple files at once in the file picker.")