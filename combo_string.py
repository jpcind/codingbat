def combo_string(a,b):
    if len(a) < len(b):
        shorter = a
        longer = b
    else:
        shorter = b
        longer = a
    return "{c}{d}{c}".format(c=shorter,d=longer)

def main():
    print(combo_string("Hello","hi"))
    print(combo_string("hi","Hello"))
    print(combo_string('aaa','b'))

main()
