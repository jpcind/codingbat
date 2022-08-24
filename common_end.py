def common_end(a,b):
    if len(a) < 1 or len(b) < 1:
        return False
    if a[0] == b[0] or a[-1] == b[-1]:
        return True
    return False

def main():
    print(common_end([1,2,3],[7,3]))
    print(common_end([1,2,3],[7,3,4]))
    print(common_end([1,2,3],[1,3]))

main()
