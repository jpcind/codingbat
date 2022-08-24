def make_out_word(out, word):
    return "{a}{b}{c}".format(a=out[:2],b=word,c=out[2:])

def main():
    print(make_out_word('<<>>','Yay'))
    print(make_out_word('[[]]','word'))

main()
