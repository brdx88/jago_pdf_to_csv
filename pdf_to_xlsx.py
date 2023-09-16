import pdfplumber
import pandas as pd

# Step 1: Read PDF and Extract Table Data
pdf_path = r"C:\Users\brian\python_automation\Jago_Main Pocket_History_27082023.pdf"

data = []
current_header = None

with pdfplumber.open(pdf_path) as pdf:
    for page_num, page in enumerate(pdf.pages):
        table = page.extract_text()
        
        print(table, "\n")
        print(table[0], "\n")

        if table:
            header = table[0]
            if not current_header or header == current_header:
                data.extend(table[1:])
                current_header = header
            else:
                # Possible table split across pages, adjust header
                current_header = header
                data[-1] += table[0]  # Combine last row of previous page with header of this page
                data.extend(table[1:])

# Step 2: Convert Table Data to DataFrame
transaction_df = pd.DataFrame(data, columns=current_header)

# Step 3: Export DataFrame to Excel
excel_output_path = r'C:\Users\brian\python_automation\transaction_history.xlsx'
transaction_df.to_excel(excel_output_path, index=False)

print("PDF data has been successfully converted and exported to Excel.")
