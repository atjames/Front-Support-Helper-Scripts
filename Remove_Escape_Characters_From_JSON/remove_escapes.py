import json


json_string_with_escapes = ""


json_data = json.loads(json_string_with_escapes)
json_string_cleaned = json.dumps(json_data, indent=4)


with open("cleaned_json.txt", "w") as file:
    file.write(json_string_cleaned)

print("Cleaned JSON has been written to cleaned_json.txt")
