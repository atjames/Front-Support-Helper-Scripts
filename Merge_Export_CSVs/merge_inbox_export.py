import os
import csv

'''

This is for a multiple inbox export. 

Please note if the exports are quite large you should consider chuncking output CSVs.This is because applications like Excel have a row limit on CSVs that is just over 1 million. 

Expected file structure is: 
Inboxes -> Inbox folder -> Conversation folder -> Messages.csv

'''

# Path to the Inboxes folder
parent_folder_path = r'file\path\here'

# Dictionary to store rows for each inbox folder
inbox_rows = {}

csv.field_size_limit(10**6)  # Increases the maximum allowable field size for CSV parsing. By default, the csv library in Python imposes a limit on the size of individual fields (cells) in a CSV file. Need to increase this due to the size of fields in the Text column of the messages.csv

try:
    # Get list of inbox folders
    inbox_folders = os.listdir(parent_folder_path)
    total_inboxes = len(inbox_folders)
    print(f"Processing {total_inboxes} inbox folders...")

    # Iterate through each inbox folder
    for inbox_folder in inbox_folders:
        inbox_folder_path = os.path.join(parent_folder_path, inbox_folder)

        if os.path.isdir(inbox_folder_path):
            # Initialize rows for the current inbox folder
            inbox_rows[inbox_folder] = []

            # Get list of conversation folders
            conversation_folders = os.listdir(inbox_folder_path)
            total_conversations = len(conversation_folders)
            print(f"Processing {total_conversations} conversation folders in {inbox_folder}...")

            # Iterate through each conversation folder
            for conversation_folder in conversation_folders:
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
                            print(f"Error reading file {messages_csv_path}: {e}")

            # Write rows for the current inbox folder to a CSV file
            if inbox_rows[inbox_folder]:
                output_csv = f'{inbox_folder}.csv'
                try:
                    with open(output_csv, mode='w', newline='', encoding='utf-8') as outfile:
                        writer = csv.writer(outfile)
                        writer.writerow(headers)
                        writer.writerows(inbox_rows[inbox_folder])

                    print(f"Written CSV for inbox folder {inbox_folder} to {output_csv}")

                except Exception as e:
                    print(f"Error writing to file {output_csv}: {e}")

except Exception as e:
    print(f"Error processing files: {e}")
