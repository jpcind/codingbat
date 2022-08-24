def string_splosion(string):
    new_string = []
    new_string2 = []
    string = list(string)
    for i in range(len(string)):
        new_string.append(string[0:i+1])
    for i in new_string:
        new_string2.append(''.join(i))
    return (''.join(new_string2))


string_splosion("Code")
string_splosion('abc')
string_splosion('ab')

