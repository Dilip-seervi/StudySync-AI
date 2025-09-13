# app.py
# StudySync AI - Prototype
# An AI-powered study assistant that answers questions from custom notes

import streamlit as st
import PyPDF2  # for PDF processing
import io

st.title("📚 StudySync AI - Prototype")
st.write("Upload your study material and ask questions. (Demo version)")

# File uploader with better error handling
uploaded_file = st.file_uploader("Upload Study Material (PDF)", type=["pdf"])

if uploaded_file is not None:
    st.success("✅ File uploaded successfully!")
    
    # Process PDF with more robust error handling
    try:
        # Create a copy of the file in memory
        file_bytes = uploaded_file.read()
        
        try:
            pdf_reader = PyPDF2.PdfReader(io.BytesIO(file_bytes))
            text_content = ""
            for page in pdf_reader.pages:
                text_content += page.extract_text()
            
            if text_content.strip():
                st.write("PDF Content Preview:")
                st.write(text_content[:500] + "...")  # Show first 500 characters
            else:
                st.warning("The PDF appears to be empty or unreadable.")
                
        except PyPDF2.PdfReadError:
            st.error("Error: The PDF file appears to be corrupted or protected.")
            
    except Exception as e:
        st.error(f"An unexpected error occurred: {str(e)}")

# Question input
question = st.text_input("Enter your question:")

if st.button("Get Answer"):
    if uploaded_file is None:
        st.warning("Please upload a PDF first!")
    elif question.strip() == "":
        st.warning("Please enter a question!")
    else:
        # Placeholder response (later will be replaced by RAG + LLM)
        st.info(f"Answer for: '{question}'")
        st.write("🤖 This is a placeholder. The AI will generate answers from your study material in the full version.")

# Future: Add 'Download Answer PDF' button
st.write("---")
st.write("🚀 Future Features:")
st.markdown("""
- Extract text from uploaded study material
- Store and retrieve chunks using **ChromaDB**
- Use **LLM (OpenAI API / Local model)** for answering
- Export neat **PDF answer sheets**
""")
