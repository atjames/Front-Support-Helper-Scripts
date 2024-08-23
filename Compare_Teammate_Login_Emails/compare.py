import csv

def convert_id(id_num):
    alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
    base36_string = ''
    id_num = int(id_num)
    while id_num:
        id_num, remainder = divmod(id_num, 36)
        base36_string = alphabet[remainder] + base36_string
        
    return 'tea_' + base36_string

def compare_csvs(csv1_path, csv2_path, output_path):
    with open(csv1_path, mode='r') as csv1_file, open(csv2_path, mode='r') as csv2_file, open(output_path, mode='w') as output_file:
        csv1_reader = csv.DictReader(csv1_file)
        csv2_reader = csv.DictReader(csv2_file)

        # Convert CSV2 to a dictionary for quick lookup
        csv2_dict = {row['ID']: row['Email'] for row in csv2_reader}

        for i, row in enumerate(csv1_reader, start=1):
            converted_id = convert_id(row['ID'])
            csv1_email = row['Email']

            # Check if the converted ID exists in CSV2
            if converted_id in csv2_dict:
                csv2_email = csv2_dict[converted_id]

                # If emails don't match, write to the output file
                if csv1_email != csv2_email and csv2_email != "N/A":
                    output_file.write(f"Row {i}: CSV1 Email: {csv1_email} | CSV2 Email: {csv2_email}\n")

# Example usage
compare_csvs(r"filepath\to\teammatetable\csv", r"filepath\to\customer\csv", 'mismatched_emails.txt')