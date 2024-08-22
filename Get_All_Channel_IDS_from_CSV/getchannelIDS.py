import pandas as pd


input_csv = 'input.csv'
output_csv = 'output.csv'


df = pd.read_csv(input_csv)


smtp_data = df[df['Type'].str.contains('SMTP', case=False, na=False)]


filtered_ids = ','.join(smtp_data['ID'].astype(str))


with open(output_csv, 'w') as file:
    file.write(filtered_ids)


num_ids_written = len(smtp_data)

print(f"Filtered IDs have been saved to {output_csv}")
print(f"Total number of IDs written to the output file: {num_ids_written}")
