def make_tags(tag, word):
    return "<{a}>{b}</{a}>".format(a=tag,b=word)

def main():
    print(make_tags('i','Yay'))

main()
