# List of private IDs
ids = [
    'evt_2dnenky2',
]

# Remove prefix and convert to private ID
for id in ids:
    print(int(id.split('_')[1], 36))