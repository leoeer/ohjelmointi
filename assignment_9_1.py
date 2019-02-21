def main():
    entry = 0
    while entry != "":
        try:
            nimi = str(input("What is your input file? "))
            tiedosto = open(nimi, "r")
            lyhyt = str(input("What is your output file #1? "))
            lyhyt_tiedosto = open(lyhyt, "w")
            pitka = str(input("What is your output file #2? "))
            pitka_tiedosto = open(pitka, "w")
            pituus = int(input("What is your threshold value? "))


            with tiedosto as f:
                for line in f:
                    num_chars = 0
                    line = line.rstrip("\n")
                    num_chars += len(line)
                    if num_chars >= pituus:
                        pitka_tiedosto.write(line + "\n")
                    elif num_chars < pituus:
                        lyhyt_tiedosto.write(line + "\n")
                    else:
                        print("Your input file contains no lines. ")

            pitka_tiedosto.close()
            lyhyt_tiedosto.close()
            print("The lines from the input file have been sorted based on your threshold value. ")
            break

        except FileNotFoundError:
            print("The file you entered was not found. Please try again.\n")

main()