from tabulate import tabulate

def flatten_json(y):
    """
    Flatten a nested JSON object.
    
    Args:
    - y (dict): The JSON object to flatten.

    Returns:
    - dict: A flattened dictionary where keys represent the nested structure.
    """
    out = {}

    def flatten(x, name=''):
        if isinstance(x, dict):
            for a in x:
                flatten(x[a], name + a + '.')
        elif isinstance(x, list):
            for i, a in enumerate(x):
                flatten(a, name + str(i) + '.')
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

def json_to_table(json_obj):
    """
    Convert a JSON object to a table with borders.
    
    Args:
    - json_obj (dict or list): The JSON object to convert.

    Returns:
    - str: The formatted table as a string.
    """
    if isinstance(json_obj, dict):
        flattened = flatten_json(json_obj)
        table = [[key, value] for key, value in flattened.items()]
    elif isinstance(json_obj, list):
        table = []
        for i, item in enumerate(json_obj):
            flattened = flatten_json(item)
            for key, value in flattened.items():
                table.append([f"{i}.{key}", value])
    else:
        table = [["Value", json_obj]]

    return tabulate(table, headers=["Key", "Value"], tablefmt="grid")

def write_json_to_txt(json_obj, output_file):
    """
    Writes a JSON object to a text file in a table format with borders.
    
    Args:
    - json_obj (dict or list): The JSON object to write.
    - output_file (str): The path to the output text file.
    """
    table_str = json_to_table(json_obj)
    with open(output_file, 'w') as file:
        file.write(table_str)

# Example usage
json_data = {
    "sender": {
        "handle": "test@gmail.com",
        "name": "Andy James",
        "author_id": 123456789
    },
    "to": [
        "harry.potter@hogwarts.edu"
    ],
    "cc": [],
    "bcc": [],
    "subject": "You're a wizard",
    "body": "You're a wizard harry",
    "body_format": "html",
    "external_id": "9999999",
    "assignee_id": None,
    "tags": [
        "Wizard",
        "Hogwarts",
        "Muggle",
        "Bald man messaging me why?"
    ],
    "type": "email",
    "created_at": 1710760821,
    "conversation_id": None,
    "metadata": {
        "thread_ref": None,
        "is_inbound": False,
        "is_archived": False,
        "should_skip_rules": True
    },
    "company_slug": "123456789",
    "inbox_id": 25885,
    "date": 1710760821000,
    "author_id": None,
    "message_id": "messges@123456.com",
    "uid": "456789123",
    "reference": "this_is_a_reference",
    "recipients": [
        {
            "role": "to",
            "handle": "harry.potter@hogwarts.edu"
        }
    ],
    "attachments": []
}

# Convert to table and save to a .txt file
output_file_path = "output_table.txt"
write_json_to_txt(json_data, output_file_path)

print(f"Table saved to {output_file_path}")
