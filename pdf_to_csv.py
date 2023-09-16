import pdfplumber
import pandas as pd
import re

# Step 1: Read PDF and Extract Text
pdf_path = r"C:\Users\brian\python_automation\Jago_Main Pocket_History_27082023.pdf"

page_texts = []

with pdfplumber.open(pdf_path) as pdf:
    for page_num, page in enumerate(pdf.pages):
        text = page.extract_text()
        page_texts.append(text)

# Step 2: Process Text and Create CSV Content
header = None
csv_content = []

for page_text in page_texts:
    lines = page_text.strip().split("\n")
    
    if not header:
        # Check if line contains the header pattern
        if "Date & Time Source/Destination Transaction Details Notes Amount Balance" in lines[1]:
            header = lines[1].split("\t")
            csv_header = "|".join(header)
    else:
        for line in lines:
            # Check if line follows the content pattern
            if re.match(r'\d{2} \w{3} \d{4}.*', line):
                content = re.split(r'\t', line, maxsplit=len(header) - 1)
                csv_line = "|".join(content)
                csv_content.append(csv_line)

# Step 3: Write Header and Data to CSV
csv_output_path = r'C:\Users\brian\python_automation\transaction_history.csv'
with open(csv_output_path, 'w') as csv_file:
    csv_file.write(csv_header + "\n")
    csv_file.write("\n".join(csv_content))

print("PDF data has been successfully converted and exported to CSV.")
