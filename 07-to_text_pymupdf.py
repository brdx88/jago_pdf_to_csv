import PyPDF2

pdf_file_path = r"C:\Users\brian\python_automation\Jago_Main Pocket_History_27082023.pdf"

with open(pdf_file_path, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

print(text)