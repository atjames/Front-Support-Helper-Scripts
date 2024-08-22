from tabulate import tabulate

def flatten_json(y):
    """
    Flatten a nested JSON object into a single-level dictionary.
    
    Args:
    - y (dict): The JSON object to flatten.

    Returns:
    - dict: A flattened dictionary where keys represent the nested structure using dot notation.
    """
    out = {}

    def flatten(x, name=''):
        # Check if the current item is a dictionary
        if isinstance(x, dict):
            for a in x:
                # Recursively flatten the dictionary, appending the key to the name
                flatten(x[a], name + a + '.')
        # Check if the current item is a list
        elif isinstance(x, list):
            for i, a in enumerate(x):
                # Recursively flatten the list, appending the index to the name
                flatten(a, name + str(i) + '.')
        else:
            # Assign the value to the output dictionary with the current name as the key
            out[name[:-1]] = x

    flatten(y)
    return out

def json_to_table(json_obj):
    """
    Convert a JSON object to a formatted table with borders.
    
    Args:
    - json_obj (dict or list): The JSON object to convert.

    Returns:
    - str: The formatted table as a string.
    """
    if isinstance(json_obj, dict):
        # Flatten the JSON object if it's a dictionary
        flattened = flatten_json(json_obj)
        # Create a table from the flattened dictionary
        table = [[key, value] for key, value in flattened.items()]
    elif isinstance(json_obj, list):
        # Initialize an empty table for a list of JSON objects
        table = []
        for i, item in enumerate(json_obj):
            # Flatten each item in the list
            flattened = flatten_json(item)
            for key, value in flattened.items():
                # Append the flattened keys and values to the table
                table.append([f"{i}.{key}", value])
    else:
        # Handle non-dict and non-list JSON objects by simply placing the value in a table
        table = [["Value", json_obj]]

    # Format the table using the `tabulate` function with grid borders
    return tabulate(table, headers=["Key", "Value"], tablefmt="grid")

def write_json_to_txt(json_obj, output_file):
    """
    Write a JSON object to a text file in a formatted table with borders.
    
    Args:
    - json_obj (dict or list): The JSON object to write.
    - output_file (str): The path to the output text file.
    """
    # Convert the JSON object to a table format
    table_str = json_to_table(json_obj)
    # Write the table string to the specified output file
    with open(output_file, 'w') as file:
        file.write(table_str)

# Example usage with a sample JSON object
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

# Convert the JSON data to a table format and save it as a .txt file
output_file_path = "output_table.txt"
write_json_to_txt(json_data, output_file_path)

print(f"Table saved to {output_file_path}")
