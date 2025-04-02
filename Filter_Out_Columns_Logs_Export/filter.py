import pandas as pd

# Load the CSV file
df = pd.read_csv(r'logs.csv')

# Select only the columns you want to keep
columns_to_keep = ['timestamp', 'iso_timestamp', 'error_details']
filtered_df = df[columns_to_keep]

# Save the filtered data to a new CSV file
filtered_df.to_csv(r'output_.csv', index=False)