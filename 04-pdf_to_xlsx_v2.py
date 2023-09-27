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

        # print(text, '\n')         di step ini berhasil baca semua tulisan line by line.

# Step 2: Process Text and Create DataFrame
header = None
data = []

for page_text in page_texts:
    lines = page_text.strip().split("\n")
    # print(lines, "\n")
    print(lines[1])
    print(lines[1].split('\t'), "\n")
    
    if not header:
        # Check if line contains the header pattern
        if "Date & Time Source/Destination Transaction Details Notes Amount Balance" in lines[1]:
            header = lines[1].split("\t")

            # print(header)
    else:
        for line in lines:
            # Check if line follows the content pattern
            if re.match(r'\d{2} \w{3} \d{4}.*', line):
                data.append(line.split("\t"))

# Step 3: Convert Data to DataFrame
transaction_df = pd.DataFrame(data, columns=header)

# Step 4: Export DataFrame to Excel
excel_output_path = r'C:\Users\brian\python_automation\transaction_history.xlsx'
transaction_df.to_excel(excel_output_path, index=False)

print("PDF data has been successfully converted and exported to Excel.")
