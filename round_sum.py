def round_sum(a, b, c):
    my_list = [a, b, c]
    new_list = []
    for i in my_list:
        rem = i % 10
        if rem <= 4:
            new_i = i - rem
            new_list.append(new_i)
        elif rem >= 5:
            rem = 10 - rem
            new_i = i + rem
            new_list.append(new_i)
    return sum(new_list)
