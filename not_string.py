def not_string(string):
    splitted_string = string.split()
    if splitted_string[0] == "not":
        return string
    else:
        return "not " + string
