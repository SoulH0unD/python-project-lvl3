def name_formation(name):
    new_name = ''
    if "https://" in name:
        name = name[8:]
    elif "http://" in name:
        name = name[7:]
    for char in name:
        if char == '.' or char == '/':
            new_name += '-'
        else:
            new_name += char
    return new_name
