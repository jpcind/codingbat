def string_match(a, b):
    count = 0
    for i in range(len(a)):
        if a[i:i+2] == b[i:i+2] and len(a[i:i+2]) == 2:
            print(a[i:i+2])
            print(b[i:i+2])
            count = count + 1
    return count






def prac():
    my_list = [1,2,3,4,5]
    print(my_list[0:0+2])

def main():
    print(string_match('abc','axc'))


main()
