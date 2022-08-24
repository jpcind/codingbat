def lucky_sum(a, b, c):
    my_list = [a, b, c]
    my_sum = 0
    for i in my_list:
        if i != 13:
            my_sum = my_sum + i
        else:
            break
    return my_sum



if __name__ == '__main__':
    print(lucky_sum(1, 13, 13))
