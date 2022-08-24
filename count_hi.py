def count_hi(string):
    count = 0
    list_string = list(string)
    for i in range(len(list_string)-1):
        if list_string[i] == 'h':
            if list_string[i+1] == 'i':
                count += 1
    return count
