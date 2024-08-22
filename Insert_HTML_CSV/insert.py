import csv

# Function to insert HTML content into the CSV file
def insert_html_into_csv(csv_file, row_index, html_content):
    with open(csv_file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    rows[row_index]['html_content'] = html_content

    with open(csv_file, 'w', newline='') as file:
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

csv_file = 'export.csv'

row_index = 0

html_content = """
THIS IS HTML CONTENT HERE!!! 
"""

insert_html_into_csv(csv_file, row_index, html_content)

print("HTML content inserted into the CSV file successfully.")
