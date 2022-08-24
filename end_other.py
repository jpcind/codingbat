def end_other(a, b):
    a = a.lower()
    b = b.lower()
    if len(a) > len(b):
        length_b = len(b)
        if b == a[-length_b:]:
            return True
    else:
        length_a = len(a)
        if a == b[-length_a:]:
            return True
    return False
