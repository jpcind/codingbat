def diff21(n):
    if n > 21:
        return abs(21-n) * 2
    answer = 21 - n
    return abs(answer)


def main():
    print(diff21(25))


main()
