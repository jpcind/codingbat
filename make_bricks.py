def make_bricks(small, big, goal):
    big_total = big * 5
    small_total = small * 1
    if big_total >= goal and goal % 5 == 0:
        return True
    if big_total <= goal:
        remainder_for_small = goal - big_total
        if small_total >= remainder_for_small:
            return True
    if big_total > goal:
        a = goal // 5
        a = a * 5
        b = a + small_total
        if b >= goal:
            return True
    return False



def main():
    print(make_bricks(6, 0, 11))


main()
