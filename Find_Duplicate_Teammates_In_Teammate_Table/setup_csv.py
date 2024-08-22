import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('teammates.csv', usecols=['ID', 'Name', 'Status'])

# Convert 'Status' column to lowercase
df['Status'] = df['Status'].str.lower()

# Filter rows with 'Status' column equals 'active'
active_df = df[df['Status'] == 'active']

# Replace missing values in the 'Name' column with empty strings
active_df['Name'].fillna('', inplace=True)

# Split the 'Name' column into first and last names
active_df[['First Name', 'Last Name']] = active_df['Name'].str.split(n=1, expand=True)

# Drop the 'Name' column
active_df.drop(columns=['Name'], inplace=True)

# Save the new DataFrame to a new CSV file
active_df.to_csv('cleaned.csv', index=False)

print("New CSV file created with First Name, Last Name, and associated ID for active teammates.")




