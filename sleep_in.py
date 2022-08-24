def sleep_in(weekday, vacation):
    # not weekday, vacation
    if weekday:
        if vacation:
            return True
        else:
            return False
    return True



if __name__ == '__main__':
    print(sleep_in(False, False))
    print(sleep_in(True, False))
    print(sleep_in(False, True))
