def missing_char(string, n):
    try:
        list_string = list(string)
        list_string.pop(n)
        return ''.join(list_string)
    except IndexError:
        return "Index out of range"

def main():
    print(missing_char('kitten',8))
    print(missing_char('kitten', 0))
    print(missing_char('kitten', 4))

main()
