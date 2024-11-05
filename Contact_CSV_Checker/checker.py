import csv
import re

# Define regex
email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
us_phone_regex_with_code = r"^1\d{10}$"
us_phone_regex_without_code = r"^\d{10}$"

def validate_email(email):
    return re.match(email_regex, email) is not None

def validate_phone(phone):
    if phone == "":
        return True
    return re.match(us_phone_regex_with_code, phone) is not None or re.match(us_phone_regex_without_code, phone) is not None

def load_account_names(account_file):
    account_names = set()
    with open(account_file, mode='r') as accounts_file:
        accounts_reader = csv.DictReader(accounts_file)
        for row in accounts_reader:
            account_names.add(row['name'])
    return account_names

def check_contact_file(input_file, output_file, account_file):
    account_names = load_account_names(account_file)
    with open(input_file, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        invalid_entries = []

        for row_index, row in enumerate(csv_reader, start=2):
            email = row['email']
            phone = row['phone']
            account_name = row['accountName']
            issues = []

            # Check if both email and phone are blank
            if not email and not phone:
                issues.append("Both email and phone are missing")

            # Validate email if present
            elif email and not validate_email(email):
                issues.append("Invalid email format")

            # Validate phone if present
            elif phone and not validate_phone(phone):
                issues.append("Invalid phone format")

            # Check if account name exists in accounts.csv
            if account_name not in account_names:
                issues.append("Account does not match any currently existing accounts")

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

input_file = r'CUSTOMER_PROVIDED_CSV'
output_file = r'invalid_contacts.txt'
account_file = r'ACCOUNT_EXPORT_FILE.CSV'
check_contact_file(input_file, output_file, account_file)