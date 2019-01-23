def main():
    print("Hello! This program helps you figure the correct form for numerical nouns in Russian. \n")
    user_input = int(input("Please enter an integer number: "))
    modulo = user_input % 100
    if user_input > 20 and user_input < 100:
        modulo = user_input % 10
    if user_input > 100:
        modulo = user_input % 100
    x = modulo
    if modulo == 1:
        print("The noun must be in nominative singluar." )
    elif x == 2 or x == 3 or x == 4:
        print("The noun must be in genitive singular." )
    elif x == 11 or x == 12 or x == 13 or x == 14:
        print("The noun must be in genitive plural")
    else:
        print("The noun must be in genitive plural. ")

main()