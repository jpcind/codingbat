def extra_end(string):
    return string[-2:] * 3

def main():
    print(extra_end('Hello'))
    print(extra_end('ab'))
    print(extra_end('Hi'))

main()
