def no_teen_sum(a, b, c):
    my_sum = 0
    my_list = [a, b, c]
    teens = [13, 14, 17, 18, 19]
    for i in my_list:
        if i not in teens:
            my_sum = my_sum + i
    return my_sum





def main():
    pass

main()
