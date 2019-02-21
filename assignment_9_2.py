import re

accepted  = [r"00\d{2}0\s(Helsinki|Helsingfors)", \
             r"01(0|[2-7])\d0\s(Vantaa|Vanda)", \
             r"02([0-3]|[6-9])\d0\s(Espoo|Esbo)", \
             r"027\d0\s(Kauniainen|Grankulla)"]

def main():
    entry = 0
    while entry != "":
        entry = str(input("Enter a postal code line of a street address: "))
        if entry == "":
            print("Bye!")
            break
        for i in accepted:
            if re.search(i, entry):
                print("Yes, this looks like a valid address in the Greater Helsinki area.\n")
                break
        else:
            print("No, this does not look like a valid address in the Greater Helsinki area.\n")

main()