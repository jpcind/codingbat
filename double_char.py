def double_char(string):
    new_list = []
    my_list = list(string)
    for i in my_list:
        new_list.append(i*2)

    return ''.join(new_list)


print(double_char("hello"))
