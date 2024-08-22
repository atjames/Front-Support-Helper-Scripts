import pandas as pd
import urllib.parse


df = pd.read_csv('input.csv') 

# Column name you want to decode
column_name = 'request.path'

def decode_url(value):
    return urllib.parse.unquote(value)

# Apply to the specified column
df[column_name] = df[column_name].apply(decode_url)

# Print to file :D
output_file_path = 'output.txt' 
df.to_csv(output_file_path, index=False)

print(f"Decoded values have been saved to {output_file_path}")