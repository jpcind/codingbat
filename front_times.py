def front_times(string, n):
    if n >= 0:
        string = list(string)
        first_letters = string[0:3]
        return ''.join(first_letters * n)


print(front_times('Chocolate',3))
