import os
import csv
from tqdm import tqdm

'''
This is for a multiple inbox export. It's a bit more code than the other Merge function. 

Please note if the export is quite large you might need to break CSVs into chunks per inbox. Applications like Excel have a row limit on CSVs just over 1 million. 

Expected file structure is: 
Inboxes -> Inbox folder -> Conversation folders -> Messages.csv

'''

# Path to the Parent folder
parent_folder_path = r'file\path\here'

# Dictionary to store rows for each inbox folder
inbox_rows = {}

# Increase the maximum field size limit
csv.field_size_limit(10**6)  # Set to a larger size if necessary

try:
    # Get list of inbox folders
    inbox_folders = os.listdir(parent_folder_path)
    total_inboxes = len(inbox_folders)
    
    # Iterate through each inbox folder with progress bar
    for inbox_folder in tqdm(inbox_folders, desc='Inbox Folders', unit='folder'):
        inbox_folder_path = os.path.join(parent_folder_path, inbox_folder)
        
        if os.path.isdir(inbox_folder_path):
            # Initialize rows for the current inbox folder
            inbox_rows[inbox_folder] = []
            
            # Get list of conversation folders
            conversation_folders = os.listdir(inbox_folder_path)
            total_conversations = len(conversation_folders)

            # Iterate through each conversation folder with progress bar
            for conversation_folder in tqdm(conversation_folders, desc=f'Processing Conversations in {inbox_folder}', unit='folder', leave=False):
                conversation_folder_path = os.path.join(inbox_folder_path, conversation_folder)

                if os.path.isdir(conversation_folder_path):
                    messages_csv_path = os.path.join(conversation_folder_path, 'messages.csv')

                    if os.path.exists(messages_csv_path):
                        try:
                            with open(messages_csv_path, mode='r', newline='', encoding='utf-8') as csvfile:
                                reader = csv.reader(csvfile)
                                headers = next(reader)  # Read and skip the header row

                                # Add new column headers
                                headers.append('Conversation ID')
                                headers.append('Inbox Folder')

                                for row in reader:
                                    # Append the current folder names as new columns
                                    row.append(conversation_folder)
                                    row.append(inbox_folder)
                                    inbox_rows[inbox_folder].append(row)

                        except Exception as e:
                            tqdm.write(f"Error reading file {messages_csv_path}: {e}")

            # Write rows for the current inbox folder to a CSV file
            if inbox_rows[inbox_folder]:
                output_csv = f'{inbox_folder}.csv'
                try:
                    with open(output_csv, mode='w', newline='', encoding='utf-8') as outfile:
                        writer = csv.writer(outfile)
                        writer.writerow(headers)
                        writer.writerows(inbox_rows[inbox_folder])

                    tqdm.write(f"Written CSV for inbox folder {inbox_folder} to {output_csv}")

                except Exception as e:
                    tqdm.write(f"Error writing to file {output_csv}: {e}")

except Exception as e:
    tqdm.write(f"Error processing files: {e}")