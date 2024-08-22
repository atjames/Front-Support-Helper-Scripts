# Define the file paths
input_file = 'input_templates.csv'
output_file = 'fixed_templates.csv'

def fix_double_encoding(text):
    # Assuming the text was encoded in ISO-8859-1 and then re-encoded into UTF-8
    # We need to decode it twice to get back to the original text
    return text.encode('ISO-8859-1').decode('utf-8')

# Read the file as binary data
with open(input_file, 'rb') as f:
    raw_data = f.read()

# Apply the double-encoding fix directly
fixed_data = fix_double_encoding(raw_data.decode('ISO-8859-1'))

# Write the correctly encoded data to a new file in UTF-8
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(fixed_data)

print("File encoding has been corrected and saved as", output_file)
