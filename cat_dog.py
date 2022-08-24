def cat_dog(string):
    cat_count = 0
    dog_count = 0
    list_string = list(string)
    for i in range(len(list_string)-2):
        if list_string[i] == 'c':
            if list_string[i+1] == 'a':
                if list_string[i+2] == 't':
                    cat_count += 1
    for i in range(len(list_string)-2):
        if list_string[i] == 'd':
            if list_string[i+1] == 'o':
                if list_string[i+2] == 'g':
                    dog_count +=1
    if dog_count == cat_count:
        return True
    return False


