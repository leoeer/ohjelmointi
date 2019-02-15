




def main():
    eng2fin = {"beer": "olut", "deer": "peura", "here": "täällä", "ear": "korva", \
               "dear": "rakas", "weird": "outo", "gear": "vaihde", "sincere": "vilpitön", \
               "clear": "kirkas", "fear": "pelko"}
    sourceword = 0
    newword = 0
    while (sourceword != "") and (newword != ""):
        sourceword = str(input("Please, enter an English word to translate into Finnish: "))
        if sourceword in eng2fin:
            translation = eng2fin[sourceword]
            print("The English word", sourceword, "is", translation, "in Finnish.\n")
        if (sourceword not in eng2fin) and (sourceword != ""):
            print("Sorry, I don't know how to translate the English word " + sourceword + " into Finnish.")
            newword = str(input("Please, teach me what the Finnish translation of " + sourceword + " is: "))
            if newword != "":
                eng2fin[sourceword] = newword
                print("Thank you, your translation was added to the dictionary.\n")
    print("Bye!")

main()