import csv
import re

# Function to extract webhook_url contained in our logs
def extract_webhook_url(webhook_details):
    match = re.search(r'"webhook_url"\s*:\s*"([^"]+)"', webhook_details)
    if match:
        return match.group(1)
    else:
        return ""


input_file = "input.csv"
output_file = "output.csv"


with open(input_file, "r", newline="", encoding="utf-8") as infile, open(output_file, "w", newline="", encoding="utf-8") as outfile:
    reader = csv.DictReader(infile)
    fieldnames = ["timestamp", "iso_timestamp", "code", "errorType", "webhook_url"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

  
    for row in reader:
        webhook_url = extract_webhook_url(row.get("message_1", ""))
        writer.writerow({
            "timestamp": row["timestamp"],
            "iso_timestamp": row["iso_timestamp"],
            "code": row["code"],
            "errorType": row["errorType"],
            "webhook_url": webhook_url
        })

print("CSV created...")
