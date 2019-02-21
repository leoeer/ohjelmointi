def main():
    entry = 0
    while entry != "":
        try:
            nimi = str(input("Please give the name of your file or the path to your file: "))
            tiedosto = open(nimi, "r")
            lines = 0
            num_words = 0
            num_chars = 0
            with tiedosto as f:
                for line in f:
                    words = line.split()
                    lines += 1
                    num_words += len(words)
                    num_chars += len(line)
            print("Number of lines in file:",lines)
            print("Number of words in file:",num_words)
            print("Number of characters in file:",num_chars)

            tiedosto.close()
            break
        except FileNotFoundError:
            print("The file you entered was not found. Please try again.\n")


main()