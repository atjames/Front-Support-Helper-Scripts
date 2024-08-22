import csv

def extract_ids(csv_file):
    ids = []
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            ids.append(row['ID'])
    return ','.join(ids)

csv_file = 'input.csv'  # Replace with your CSV file name
print(extract_ids(csv_file))
