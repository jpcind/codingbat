def monkey_trouble(a_smile, b_smile):
    if a_smile != b_smile:
        return False
    return True


if __name__ == '__main__':
    print(monkey_trouble(True, True))
    print(monkey_trouble(False, False))
    print(monkey_trouble(True, False))
