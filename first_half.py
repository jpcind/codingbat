def first_half(string):
    half_length = int(len(string) / 2)
    return string[:half_length]

def main():
    print(first_half("WooHoo"))
    print(first_half("HelloThere"))
    print(first_half("abcdef"))
    print(first_half(""))


main()
