import csv

# Input and output file paths
input_file = r'input_file.csv'  # Replace with your semi-colon-separated file path
output_file = r'output_file.csv'  # Replace with your desired CSV output path

# Open the input file to read and the output file to write
with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
        open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    
    # Initialize the reader and writer
    reader = csv.reader(infile, delimiter=';')  # Read with semi-colon separator
    writer = csv.writer(outfile)  # Write with default comma separator

    # Write each row from the input file to the output CSV
    for row in reader:
        writer.writerow(row)

print(f'File converted to CSV and saved as {output_file}')