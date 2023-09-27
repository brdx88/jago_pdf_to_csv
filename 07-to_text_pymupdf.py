import PyPDF2
import re

pdf_file_path = r"C:\Users\brian\python_automation\Jago_Main Pocket_History_27082023.pdf"
output_file_path = "transaction_output_pypdf2.txt"  # Specify the output file path
start_line_number = 20  # Specify the line number to start capturing

# Define a list of lines to skip
lines_to_skip = [
    "Pockets	Transactions",
    "History",
    "Date	&	Time",
    "Source/Destination",
    "Transaction	Details",
    "Notes",
    "Amount",
    "Balance",
    "PT	Bank	Jago	Tbk	is	licensed	and	supervised	by	Financial	Services	Authority	(OJK),	and	also	a	member	of",
    "Indonesia	Deposit	Insurance	Corporation	(LPS)	deposit	insurance	program.",
    "www.jago.com",
    "Disclaimer",
    "based	on	search	result	and	filter	Customer	has	applied."
]

# Regular expression pattern to match "Page X of Y" lines
page_number_pattern = re.compile(r"Page\s+\d+\s+of\s+\d+")

with open(pdf_file_path, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    transaction_data = []
    current_line_number = 0

    for page in pdf_reader.pages:
        page_text = page.extract_text()
        lines = page_text.split('\n')

        for line in lines:
            current_line_number += 1

            # Skip lines before the specified start line
            if current_line_number < start_line_number:
                continue

            # Skip lines that match the lines to skip or the page number pattern
            if any(skip_line in line for skip_line in lines_to_skip) or page_number_pattern.match(line):
                continue

            # Add the line to transaction data
            transaction_data.append(line)

# Save the extracted transaction data to a text file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for line in transaction_data:
        output_file.write(line + '\n')

print(f"Transaction data extracted from PDF and saved to {output_file_path}")
