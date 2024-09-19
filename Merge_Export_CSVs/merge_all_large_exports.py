import os
import csv
import io
import re
import zipfile
from tqdm import tqdm

# Path to the Parent ZIP folder
parent_zip_folder_path = r'C:\Users\atjam\OneDrive\Desktop\Parent'
output_folder_path = os.path.join(parent_zip_folder_path, 'output')

# Create the output directory if it doesn't exist
os.makedirs(output_folder_path, exist_ok=True)

# Dictionary to store rows and row counts for each inbox folder
inbox_rows = {}
inbox_row_counts = {}

# Increase the maximum field size limit
csv.field_size_limit(10 * 1024 * 1024)  # 10 MB

def clean_file(file_path):
    """Read a file and replace null bytes."""
    with open(file_path, 'rb') as f:
        content = f.read()
    if b'\x00' in content:
        print(f"Null byte found in file: {file_path}")
    content = content.replace(b'\x00', b'')  # Remove null bytes
    return content.decode('utf-8', errors='ignore')  # Decode to string, ignoring decoding errors

def process_zip(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # Extract the ZIP file to a temporary directory within the output folder
        temp_dir = os.path.join(output_folder_path, os.path.basename(zip_path).rstrip('.zip'))
        zip_ref.extractall(temp_dir)
        return temp_dir

try:
    # Get list of ZIP files in the parent ZIP folder (before any extraction starts)
    zip_files = [f for f in os.listdir(parent_zip_folder_path) if f.endswith('.zip')]
    
    # Iterate through each ZIP file with progress bar
    for zip_file in tqdm(zip_files, desc='ZIP Files', unit='zip'):
        zip_file_path = os.path.join(parent_zip_folder_path, zip_file)
        
        try:
            # Process the ZIP file and get the temporary directory path
            temp_dir = process_zip(zip_file_path)

            # Get list of inbox folders within the extracted ZIP folder
            inboxes_folder_path = os.path.join(temp_dir, 'inboxes')
            if not os.path.exists(inboxes_folder_path):
                tqdm.write(f"'inboxes' folder not found in {zip_file}")
                continue

            inbox_folders = os.listdir(inboxes_folder_path)
            
            for inbox_folder in tqdm(inbox_folders, desc='Inbox Folders', unit='folder'):
                inbox_folder_path = os.path.join(inboxes_folder_path, inbox_folder)
                
                if os.path.isdir(inbox_folder_path):
                    # Initialize rows and row count for the current inbox folder
                    inbox_rows[inbox_folder] = []
                    inbox_row_counts[inbox_folder] = 0
                    
                    # Try to get the alphanumeric inbox ID from the folder name
                    match = re.search(r'inb_([a-zA-Z0-9]+)', inbox_folder)
                    if match:
                        inbox_id = "inb_" + match.group(1)
                    else:
                        tqdm.write(f"Could not extract inbox ID from folder name: {inbox_folder}")
                        continue
                    
                    # Get list of conversation folders
                    conversation_folders = os.listdir(inbox_folder_path)

                    for conversation_folder in tqdm(conversation_folders, desc=f'Processing Conversations in {inbox_folder}', unit='folder', leave=False):
                        conversation_folder_path = os.path.join(inbox_folder_path, conversation_folder)

                        if os.path.isdir(conversation_folder_path):
                            messages_csv_path = os.path.join(conversation_folder_path, 'messages.csv')

                            if os.path.exists(messages_csv_path):
                                try:
                                    # Clean file content and process
                                    cleaned_content = clean_file(messages_csv_path)
                                    cleaned_file = io.StringIO(cleaned_content)
                                    reader = csv.reader(cleaned_file, quoting=csv.QUOTE_MINIMAL)
                                    headers = next(reader)  # Read and skip the header row

                                    # Add new column headers
                                    headers.append('Conversation ID')
                                    headers.append('Inbox Folder')

                                    for row in reader:
                                        # Append the current folder names as new columns
                                        row.append(conversation_folder)
                                        row.append(inbox_id)
                                        inbox_rows[inbox_folder].append(row)
                                        inbox_row_counts[inbox_folder] += 1

                                except Exception as e:
                                    tqdm.write(f"Error reading file {messages_csv_path}: {e}")

                    # Write or append rows for the current inbox folder to a CSV file in the output directory
                    output_csv = os.path.join(output_folder_path, f'{inbox_id}.csv')
                    file_exists = os.path.isfile(output_csv)
                    
                    if file_exists:
                        tqdm.write(f"Output file {output_csv} already exists. Appending to the existing file.")

                    try:
                        with open(output_csv, mode='a' if file_exists else 'w', newline='', encoding='utf-8') as outfile:
                            writer = csv.writer(outfile, quoting=csv.QUOTE_MINIMAL)
                            if not file_exists:
                                writer.writerow(headers)  # Write headers only if the file is new
                            writer.writerows(inbox_rows[inbox_folder])
                        action = "Appended to" if file_exists else "Written"
                        tqdm.write(f"{action} CSV for inbox folder {inbox_folder} to {output_csv}")
                        tqdm.write(f"Total rows read for {inbox_id}: {inbox_row_counts[inbox_folder]}")

                    except Exception as e:
                        tqdm.write(f"Error writing to file {output_csv}: {e}")
        
        except zipfile.BadZipFile:
            tqdm.write(f"Skipping file {zip_file} as it is not a valid ZIP file.")
            continue

except Exception as e:
    tqdm.write(f"Error processing files: {e}")