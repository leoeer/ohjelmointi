def main():
    print("Hello!")
    word = 0
    while word != "":
        word = (str(input("Enter an English regular verb to inflect: ")))
        if len(word) > 0:
            infinitive(word)
            prtense(word)
            past_tense(word)
            gerund(word)
    print("Goodbye!")

def infinitive(word):
    print("Infinitive:", word,)
    return word

def prtense(word):
    paate1 = "s"
    if word.endswith(('o', 'ch', 's', 'sh', 'x', 'z')):
        paate1 = "es"
        newword = word + paate1
    elif word.endswith(('ay', 'ey', 'iy', 'oy' 'uy',)):
        paate1 = "s"
        newword = word + paate1
    elif word.endswith('y'):
        paate1 = "ies"
        newword = word[:-1] + paate1
    else:
        newword = word + paate1
    print("Pres. 3 sg:",newword)
    return word

def past_tense(word):
    paate2 = "ed"
    num_of_vow = count_vowel(word)
    vow_suffix = count_last_vowel(word)
    vikakirjain = karsi_vikat(word)
    if (num_of_vow == 1) and (vow_suffix == 1) and (vikakirjain == 0):
        newword = word + word[-1] + paate2
    elif word.endswith(('ay', 'ey', 'iy', 'oy' 'uy',)):
        paate2 = "ed"
        newword = word + paate2
    elif word.endswith('y'):
        paate2 = "ied"
        newword = word[:-1] + paate2
    elif word.endswith('e'):
        newword = word[:-1] + paate2
    elif word.endswith('ie'):
        newword = word[:-1] + paate2
    else:
        newword = word + paate2
    print("Past:",newword)
    return word

def gerund(word):
    # In this function I decided to use find instead of endswith.
    paate3 = "ing"
    num_of_vow = count_vowel(word)
    vow_suffix = count_last_vowel(word)
    vikakirjain = karsi_vikat(word)
    if (num_of_vow == 1) and (vow_suffix == 1) and (vikakirjain == 0):
        newword = word + word[-1] + paate3
    elif word.find('ie') == (len(word) - 2):
        paate3 = "ying"
        newword = word[:-2] + paate3
    elif word.find('e') == (len(word) - 1):
        newword = word[:-1] + paate3
    else:
        newword = word + paate3
    print("Gerund:", newword)
    return word

def count_vowel(word):
    vowels = 'aeiouyAEIOUY'
    count = 0
    for i in word:
        if i in vowels:
            count += 1
    return count

def count_last_vowel(word):
    vowels = 'aeiouyAEIOUY'
    count = 0
    for i in word[-2]:
        if i in vowels:
            count += 1
    return count

def karsi_vikat(word):
    vikat = 'hjwxHJWX'
    count = 0
    for i in word[-1]:
        if i in vikat:
            count += 1
    return count


main()




