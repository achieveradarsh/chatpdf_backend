import PyPDF2
from gensim.summarization import summarize
from transformers import pipeline

summarized_text = ""

def summarize_pdf(pdf_file):
    global summarized_text
    reader = PyPDF2.PdfReader(pdf_file)
    full_text = ''
    
    for page in reader.pages:
        full_text += page.extract_text()

    summary = summarize(full_text, word_count=150)
    summarized_text = full_text  # Store full text for Q&A
    return summary

def answer_question(question):
    qa_pipeline = pipeline("question-answering")
    result = qa_pipeline(question=question, context=summarized_text)
    return result['answer']
