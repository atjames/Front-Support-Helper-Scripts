import csv
import re

#Define regex
email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"  # Email format: alphanumeric characters, '.', '_', '%', '+', '-', '@', domain, and 2+ char top-level domain
us_phone_regex_with_code = r"^1\d{10}$"  # U.S. format with country code: 1XXXXXXXXXX - WILL NEED TO ADJUST FOR NUMBERS OUTSIDE THE US
us_phone_regex_without_code = r"^\d{10}$"  # U.S. format without country code: XXXXXXXXXX - WILL NEED TO ADJUST FOR NUMBERS OUTSIDE THE US

def validate_email(email):
    return re.match(email_regex, email) is not None

def validate_phone(phone):
    # Accept formats: 1XXXXXXXXXX, XXXXXXXXXX, or blank
    if phone == "":
        return True  # Allow blank phone numbers
    return re.match(us_phone_regex_with_code, phone) is not None or re.match(us_phone_regex_without_code, phone) is not None

def check_contact_file(input_file, output_file):
    with open(input_file, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        invalid_entries = []

        for row_index, row in enumerate(csv_reader, start=2):  # Start from 1 to reflect actual CSV indexing
            email = row['email']
            phone = row['phone']
            issues = []

            if not email or not validate_email(email):
                issues.append("Invalid or missing email")

            if not validate_phone(phone):
                issues.append("Invalid phone format")

            if issues:
                invalid_entries.append({
                    "index": row_index,
                    "row": row,
                    "issues": ", ".join(issues)
                })

        with open(output_file, mode='w') as out_file:
            for entry in invalid_entries:
                row_info = ", ".join(f"{k}: {v}" for k, v in entry["row"].items())
                out_file.write(f"Index {entry['index']} - Issues: {entry['issues']} - Data: {row_info}\n")

    print(f"Validation completed. See {output_file} for results.")

input_file = r'customer_provided_csv_here.csv'
output_file = r'invalid_contacts.txt'
check_contact_file(input_file, output_file)