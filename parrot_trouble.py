def parrot_trouble(talking, hour):
    if talking:
        if hour < 7 or hour > 20:
            return True
        else:
            return False
    else:
        return False



def main():
    print(parrot_trouble(True, 6))
    print(parrot_trouble(True, 7))
    print(parrot_trouble(False, 6))


main()
