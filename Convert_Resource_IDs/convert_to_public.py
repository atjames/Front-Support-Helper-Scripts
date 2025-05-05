def convert_to_base36(id_num):

    alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
    base36_string = ''
    
    while id_num:
        id_num, remainder = divmod(id_num, 36)
        base36_string = alphabet[remainder] + base36_string
    return base36_string


# List of private IDs that need to be converted
ids = [
   123456789
];

for id in ids:
    print('msg_' + convert_to_base36(id)) #change the prefix to watever the object is. remove prefix if not needed