from pdfquery import PDFQuery
import json

def extract_table(pdf, table_selector):
    table_elements = pdf.pq(table_selector)
    print(table_elements)
    rows = []
    
    for row_element in table_elements.children('LTTextLineHorizontal'):
        cells = [cell.text.strip() for cell in row_element.children('LTTextBoxHorizontal')]
        rows.append(cells)

    return rows

# def save_table_to_json(table_data, output_json_path):
#     table_json = json.dumps(table_data, indent=2, ensure_ascii=False)
#     with open(output_json_path, 'w', encoding='utf-8') as json_file:
#         json_file.write(table_json)

# Example usage     
pdf = PDFQuery('adbl.pdf')
pdf.load()
print(pdf)
# # Specify the CSS-like selector for the table
# table_selector = 'LTPage[pageid=\'1\'] LTTable[width="400.00"]'

# # Extract the table data
# table_data = extract_table(pdf, table_selector)

# # Specify the output JSON file path
# output_json_path = 'extracted_table.json'

# Save the extracted table data to a JSON file
# save_table_to_json(table_data, output_json_path)

# print(f"Extracted table saved to: {output_json_path}")
