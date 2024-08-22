import os
import csv


top_folder_path = r'/your/export_folder/here'
output_csv = 'combined_filtered_messages.csv'
filtered_rows = []

for conversation_folder in os.listdir(top_folder_path):
    conversation_folder_path = os.path.join(top_folder_path, conversation_folder)
    
    if os.path.isdir(conversation_folder_path):
        
        messages_csv_path = os.path.join(conversation_folder_path, 'messages.csv')
        if os.path.exists(messages_csv_path):
            with open(messages_csv_path, mode='r', newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                
                # Get indices of the relevant columns from header row
                header = next(reader)
                from_idx = header.index('From')
                to_idx = header.index('To')
                subject_idx = header.index('Subject')
                text_idx = header.index('Text')
                
                for row in reader:
                    # If LEED is in any of the relevant columns
                    if ("LEED" in row[from_idx] or
                        "LEED" in row[to_idx] or
                        "LEED" in row[subject_idx] or
                        "LEED" in row[text_idx]):
                      

                        #print("Found!") USED FOR DEBUGGING THAT'S WHY IT'S COMMENTED OUT :D 

                        # add the conversation folder name as a new column Conversation Folder for tracking pursposes
                        row.append(conversation_folder)
                        filtered_rows.append(row)


with open(output_csv, mode='w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(header + ['Conversation Folder'])
    writer.writerows(filtered_rows)

print(f"Filtered CSV written to {output_csv}")