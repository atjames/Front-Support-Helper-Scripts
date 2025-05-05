# List of public IDs
ids = [
    'cnv_12345689'
]

# Remove prefix and convert to private ID
for id in ids:
    print(int(id.split('_')[1], 36))