import re

exp = ['([A-Za-z|ää|öö])\\1',   'ks',   'ts',   'k(u[aeiouy])',   'k',   'j',   '[ä|ö]']
exp2 = ['\\1',   'x',   'z',   'q\\1',   'c',   'i',   'e']


def edit_file(teksti, tiedosto2, ofile):
    print("Modifying spelling and writing to file", ofile, "...")
    teksti = teksti.lower()
    for i, e in zip(exp, exp2):
            teksti = re.sub(i, e, teksti)
    tiedosto2.write(teksti)





def main():
    while True:
        try:
            ifile = str(input("Enter your input file: "))
            tiedosto1 = open(ifile, "r")
            ofile = input("Enter your output file: ")
            with tiedosto1 as f:
                teksti = f.read()
                tiedosto2 = open(ofile, "w")
                edit_file(teksti, tiedosto2, ofile)
                print("Done!")

            tiedosto1.close()
            tiedosto2.close()
            break



        except FileNotFoundError:
            print("The file you entered was not found. Please try again.\n")



main()