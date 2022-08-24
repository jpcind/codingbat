def cigar_party(cigars, is_weekend):
    if is_weekend and cigars >= 40:
        return True
    elif not is_weekend:
        if 40 <= cigars <= 60:
            return True
    return False


def main():
    pass

main()
