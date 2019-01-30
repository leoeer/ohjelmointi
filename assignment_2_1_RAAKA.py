def main():
    word = str(input("Please, enter an English word to translate into Finnish: "))
    if word == "beer":
        translation = "olut"
        print("The English word", word, "is", translation, "in Finnish.")
    elif word == "deer":
        translation = "peura"
        print("The English word", word, "is", translation, "in Finnish.")
    elif word == "here":
        translation = "täällä"
        print("The English word", word, "is", translation, "in Finnish.")
    elif word == "ear":
        translation = "korva"
        print("The English word", word, "is", translation, "in Finnish.")
    elif word == "dear":
        translation = "rakas"
        print("The English word", word, "is", translation, "in Finnish.")
    elif word == "weird":
        translation = "outo"
        print("The English word", word, "is", translation, "in Finnish.")
    elif word == "gear":
        translation = "vaihde"
        print("The English word", word, "is", translation, "in Finnish.")
    elif word == "sincere":
        translation = "vilpitön"
        print("The English word", word, "is", translation, "in Finnish.")
    elif word == "clear":
        translation = "kirkas"
        print("The English word", word, "is", translation, "in Finnish.")
    elif word == "fear":
        translation = "pelko"
        print("The English word", word, "is", translation, "in Finnish.")
    else:
        print("Sorry, I don't know how to translate the English word", word, "into Finnish.")


main()