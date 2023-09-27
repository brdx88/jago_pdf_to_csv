import PyPDF2

pdf_file_path = r"C:\Users\brian\python_automation\Jago_Main Pocket_History_27082023.pdf"
output_file_path = "transaction_output_pypdf2.txt"  # Specify the output file path

with open(pdf_file_path, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

# Save the extracted text to a text file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(text)

print(f"Text extracted from PDF and saved to {output_file_path}")
