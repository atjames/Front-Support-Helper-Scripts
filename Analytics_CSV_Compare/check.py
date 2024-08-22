import pandas as pd


df1 = pd.read_csv(r'path\to\csv1')
df2 = pd.read_csv(r'path\to\csv2')


unique_to_df1 = df1[~df1['Conversation ID'].isin(df2['Conversation ID'])]

unique_to_df2 = df2[~df2['Conversation ID'].isin(df1['Conversation ID'])]

# Save the results to new CSV files (optional)
unique_to_df1.to_csv('unique_to_df1.csv', index=False)
unique_to_df2.to_csv('unique_to_df2.csv', index=False)

'''
Optional Print for console debugging

print(unique_to_df1['Conversation ID'])
print("\nUnique to file2.csv:")
print(unique_to_df2)

'''
