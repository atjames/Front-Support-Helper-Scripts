import os
import csv


top_folder_path = r'/your/export_folder/here'
output_csv = 'combined_messages.csv'
all_rows = []
for conversation_folder in os.listdir(top_folder_path):
    conversation_folder_path = os.path.join(top_folder_path, conversation_folder)
    
    if os.path.isdir(conversation_folder_path):
        
        messages_csv_path = os.path.join(conversation_folder_path, 'messages.csv')
        if os.path.exists(messages_csv_path):
            with open(messages_csv_path, mode='r', newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)
                
                for row in reader:
                    # Append the conversation folder name as a new column
                    row.append(conversation_folder)
                    all_rows.append(row)


with open(output_csv, mode='w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['ID', 'Public ID', 'Ext ID', 'URL', 'Type', 'Source', 'Status', 'From', 'To', 'Subject', 'Text', 'Date', 'Conversation Folder'])
    writer.writerows(all_rows)

print(f"Combined CSV written to {output_csv}")