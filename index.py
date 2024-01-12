import tabula
import fitz  # PyMuPDF

# PDF file to extract tables from
file = "adbl.pdf"

# Extract text from the specific page (page number 104) using PyMuPDF
page_number = 104
text = ""
with fitz.open(file) as pdf_doc:
    page = pdf_doc[page_number - 1]  # Adjusting for 0-based indexing
    text = page.get_text()

# Use tabula to extract tables from the extracted text
tables = tabula.read_pdf(file, pages=page_number)

# Print and save the extracted tables
print(tables)
for i, table in enumerate(tables):
    print(f"Table {i + 1}:\n", table)
    table.to_json(f"adbl_table_{i + 1}_page_{page_number}.json", index=False)
