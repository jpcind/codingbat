def xyz_there(string):
    list_string = list(string)
    for i in range(len(list_string)-2):
        if list_string[i] == 'x':
            if list_string[i+1] == 'y':
                if list_string[i+2] == 'z':
                    if list_string[i-1] != '.':
                        return True
    return False
