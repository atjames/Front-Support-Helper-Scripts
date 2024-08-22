import pandas as pd

df = pd.read_csv('cleaned.csv')  # Make sure to use the cleaned CSV file or I will get very mad. (jk this just won't work as expected)

# Find rows with duplicate first and last names
duplicate_names = df[df.duplicated(subset=['First Name', 'Last Name'], keep=False)]

# Set to store processed pairs
processed_pairs = set()

# Write the rows with duplicate first and last names to a text file
with open('duplicate_names.txt', 'w') as f:
    f.write("Duplicate Names Detected:\n")
    for index, row in duplicate_names.iterrows():
        # Check if the pair has already been processed
        if (row['First Name'], row['Last Name']) not in processed_pairs:
            # Find all rows with the same first and last names
            duplicate_rows = df[(df['First Name'] == row['First Name']) & (df['Last Name'] == row['Last Name'])]
            for _, duplicate_row in duplicate_rows.iterrows():
                duplicate_row_text = f"ID: {duplicate_row['ID']}, First Name: {duplicate_row['First Name']}, Last Name: {duplicate_row['Last Name']}\n"
                f.write(f"Duplicate: {duplicate_row_text}")
            # Add processed pair to the set
            processed_pairs.add((row['First Name'], row['Last Name']))
            
print("Duplicate names detected and written to 'duplicate_names.txt'.")
