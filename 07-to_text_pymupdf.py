import fitz
import chardet

pdf_file_path = r"C:\Users\brian\python_automation\Jago_Main Pocket_History_27082023.pdf"
pdf_document = fitz.open(pdf_file_path)

text = ""

for page_number in range(pdf_document.page_count):
    page = pdf_document.load_page(page_number)
    text += page.get_text()

# Detect the encoding using chardet
detected_encoding = chardet.detect(text.encode())['encoding']

# Decode the text using the detected encoding
text = text.encode(detected_encoding, 'replace').decode('utf-8', 'replace')

pdf_document.close()

print(text)