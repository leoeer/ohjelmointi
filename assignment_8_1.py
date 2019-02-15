def main():
    print("Hello and welcome to Calculator Simplissimus!")
    uinput = 0
    while uinput != "":
        try:
            uinput = input(str("Next calculation: "))
            lasku = uinput.split()      #
            luku1 = float(lasku[0])     #
            luku2 = float(lasku[2])     #
            operator = lasku[1]         # To make string characters usable
            if operator == "+":
                print(luku1 + luku2)
            elif operator == "-":
                print(luku1 - luku2)
            elif operator == "*":
                print(luku1 * luku2)
            elif operator == "/":
                print(luku1 / luku2)
        except ValueError:
            print("You seem to have entered your calculation in the wrong form.\n" \
              "Please enter calculations in this form: 1 + 2")
        except IndexError:
            if uinput == "":
                print("Bye!")
            else:
                print("Your calculation was incomplete. Please enter calculations in\n" \
                  "this form: 1 + 2")
        except ZeroDivisionError:
            if (luku1 < 0) and (operator == "/") and (luku2 == 0):
                print("-Infinity")
            elif (luku1 > 0) and (operator == "/") and (luku2 == 0):
                print("Infinity")
            elif (luku1 == 0) and (operator == "/") and (luku2 == 0):
                print("Undefined")





main()