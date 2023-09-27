import PyPDF2

pdf_file_path = r"C:\Users\brian\python_automation\Jago_Main Pocket_History_27082023.pdf"
output_file_path = "transaction_output_pypdf2.txt"  # Specify the output file path
start_line_number = 20  # Specify the line number to start capturing

with open(pdf_file_path, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    transaction_data = []
    current_line_number = 0

    for page in pdf_reader.pages:
        page_text = page.extract_text()
        lines = page_text.split('\n')

        for line in lines:
            current_line_number += 1
            if current_line_number >= start_line_number:
                transaction_data.append(line)

# Save the extracted transaction data to a text file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for line in transaction_data:
        output_file.write(line + '\n')

print(f"Transaction data extracted from PDF and saved to {output_file_path}")
