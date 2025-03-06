'''

pip install pdfminer
pip install pdfminer.six required for extract_text

'''
from pdfminer.high_level import extract_text
import pdfminer
import re


def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

def extract_name_from_resume(text):
    name = None

    # Use regex pattern to find a potential name
    pattern = r"(\b[A-Z][a-z]+\b)\s(\b[A-Z][a-z]+\b)"
    match = re.search(pattern, text)
    if match:
        name = match.group()

    return name

def extract_contact_number_from_resume(text):
    contact_number = None

    # Use regex pattern to find a potential contact number
    pattern = r"\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b"
    match = re.search(pattern, text)
    if match:
        contact_number = match.group()

    return contact_number

if __name__ == '__main__':
    text = extract_text_from_pdf(r"power-bi-professional-resume-example.pdf")
    #text = extract_text_from_pdf(r"power-bi-standout-resume-example.pdf")
    #text = extract_text_from_pdf(r"Untitled-resume.pdf")
    name = extract_name_from_resume(text)
    
    if name:
        print("Name:", name)
    else:
        print("Name not found")
    
    contact_number = extract_contact_number_from_resume(text)

    if contact_number:
        print("Contact Number:", contact_number)
    else:
        print("Contact Number not found")