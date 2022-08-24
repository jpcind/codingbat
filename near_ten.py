def near_ten(num):
    my_rem = num % 10
    if my_rem <= 2 or 8 <= my_rem <= 9:
        return True
    return False

print(near_ten(19))
