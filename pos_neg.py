def pos_neg(a,b,negative):
    if negative:
        if a < 0 and b < 0 or a > 0 and b > 0:
            return True
        return False
    else:
        if a is not b:
            return True
        return False

def pos_neg2(a,b,negative):
    if negative:
        if a < 0 and b < 0:
            return True
        if a < 0 < b or a > 0 > b:
            return False
    if (a > 0 > b) or (a < 0 < b):
        return True
    return False

def main():
    print(pos_neg2(-4, 5, True))
    print(pos_neg2(1, -1, True))
    print(pos_neg2(-1, 1, True))

main()
