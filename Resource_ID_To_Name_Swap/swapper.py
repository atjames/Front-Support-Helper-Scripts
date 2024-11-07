import csv

# File paths for your main CSV, reference CSV, and output files
customer_provided_csv_path = r'file_path_here' # Example header row: name,namespace,highlight,parent 
tag_export_path = r'file_path_here' # Example header row: "id","name","ownerId","ownerName","ownerType"
output_csv_path = r'updated_main.csv'
unmatched_csv_path = r'unmatched_rows.csv'


reference_data = {}
with open(tag_export_path, mode='r', newline='') as reference_file:
    reader = csv.DictReader(reference_file)
    for row in reader:
        name = row['name']
        id_value = row['id']
        reference_data[name] = id_value


with open(customer_provided_csv_path, mode='r', newline='') as main_file, \
     open(output_csv_path, mode='w', newline='') as output_file, \
     open(unmatched_csv_path, mode='w', newline='') as unmatched_file:

    reader = csv.DictReader(main_file)
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    unmatched_writer = csv.DictWriter(unmatched_file, fieldnames=fieldnames)

    
    writer.writeheader()
    unmatched_writer.writeheader()
    
    
    for row in reader:
        parent_name = row['parent']
        if parent_name in reference_data:
            row['parent'] = reference_data[parent_name]  
            writer.writerow(row)  
        else:
            unmatched_writer.writerow(row)  

print(f"Updated CSV with matches saved to {output_csv_path}")
print(f"Unmatched rows saved to {unmatched_csv_path}")