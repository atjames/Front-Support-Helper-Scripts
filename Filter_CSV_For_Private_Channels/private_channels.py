import pandas as pd

df = pd.read_csv('channel_export.csv')

filtered_df = df[df['is_private'] == True]


result_df = filtered_df[['is_private', 'ID', 'Type', 'Owner', 'Send As']]

result_df.to_csv('private_channels_modified.csv', index=False)