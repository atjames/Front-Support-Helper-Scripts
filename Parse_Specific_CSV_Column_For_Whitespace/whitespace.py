import pandas as pd

# Load the CSV file
df = pd.read_csv('channels.csv')

# Filter rows where 'Send As' column contains a trailing white space after @equipmentshare.com
filtered_df = df[df['Send As'].str.contains(r'gmail\.com $')]

# Select only the 'ID' and 'Send As' columns
result_df = filtered_df[['ID', 'Send As']]

# Save the filtered data into a new CSV file
result_df.to_csv('filtered_file.csv', index=False)
