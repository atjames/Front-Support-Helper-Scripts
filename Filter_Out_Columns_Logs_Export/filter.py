import pandas as pd

# Load the CSV file
df = pd.read_csv(r'input_logs.csv')

# Select only the columns you want to keep
columns_to_keep = ['coulmn_name_to_keep_1', 'column_name_to_keep_2']
filtered_df = df[columns_to_keep]

# Save the filtered data to a new CSV file
filtered_df.to_csv(r'output_.csv', index=False)