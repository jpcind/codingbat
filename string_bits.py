def string_bits(string):
    string = list(string)
    new_string = []
    for i in range(len(string)):
        if i % 2 == 0:
            new_string.append(string[i])
    return ''.join(new_string)

