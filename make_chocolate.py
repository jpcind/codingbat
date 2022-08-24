def make_chocolate(small, big, goal):
    big_total = big * 5
    small_total = small * 1
    if big_total <= goal:
        rem = goal - big_total
        if small_total >= rem:
            return rem
    if big_total > goal:
        rem = goal % 5
        if small_total >= rem:
            return rem
    return -1


def main():
    pass


main()
