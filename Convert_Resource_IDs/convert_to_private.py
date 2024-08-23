# List of private IDs
ids = [
    '',
]

# Remove prefix and convert to private ID
for id in ids:
    print(int(id.split('_')[1], 36))