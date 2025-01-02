import csv
import json

def extract_unique_ids_from_csv(file_path):
    folder_ids_set = set()
    answer_ids_set = set()

    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            try:
                # Parse the JSON object from the 'request' column
                request = json.loads(row['request'])
                body = json.loads(request.get('body', '{}'))

                folder_ids_set.update(body.get('folder_ids', []))
                answer_ids_set.update(body.get('answer_ids', []))

            except (json.JSONDecodeError, KeyError, AttributeError) as e:
                print(f"Error processing row: {row}. Error: {e}")

    print("Unique folder_ids:")
    print(sorted(folder_ids_set))

    print("\nUnique answer_ids:")
    print(sorted(answer_ids_set))

extract_unique_ids_from_csv(r'your_file.csv')