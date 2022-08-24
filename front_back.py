def front_back(string):
    if len(string) < 1:
        return string
    string = list(string)
    string[0], string[-1] = string[-1], string[0]
    string = ''.join(string)
    return string

def main():
    print(front_back(''))

main()
