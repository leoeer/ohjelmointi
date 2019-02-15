

def make_dicts(input, dicti):
    for i in input:
        if i in dicti:
            dicti[i] += 1
        else:
            dicti[i] = 1
    return dicti

def find_matches(dic1, dic2):
    for k in dic1:
        if k in dic2:
           dic1[k] = str(dic1[k]) + ' *'
           dic2[k] = str(dic2[k]) + ' *'
    return dic1, dic2

def main():
    eka = str(input("Enter first string: "))
    toka = str(input("Enter second string: "))
    print("Character frequencies: ")
    char1 = {}
    char2 = {}
    make_dicts(eka, char1)
    make_dicts(toka, char2)
    find_matches(char1, char2)
    final = {**char1, **char2}
    for i in sorted(final.keys()):
        print("%s: %s" % (i, final[i]))


main()