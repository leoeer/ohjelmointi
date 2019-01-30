def main():
    word = str(input("Please, enter an English word to translate into Finnish: "))
    if word == "beer":
        translation = "olut"
    elif word == "deer":
        translation = "peura"
    elif word == "here":
        translation = "täällä"
    elif word == "ear":
        translation = "korva"
    elif word == "dear":
        translation = "rakas"
    elif word == "weird":
        translation = "outo"
    elif word == "gear":
        translation = "vaihde"
    elif word == "sincere":
        translation = "vilpitön"
    elif word == "clear":
        translation = "kirkas"
    elif word == "fear":
        translation = "pelko"
    else:
        translation = 0
    if translation == 0:
        print("Sorry, I don't know how to translate the English word", word, "into Finnish.")
    else:
        print("The English word", word, "is", translation, "in Finnish.")

main()