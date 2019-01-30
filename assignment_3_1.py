def main():
    import random
    secret_number = random.randint(1, 100)
    guess = int(input("Guess the number: "))
    a = int(secret_number)
    while guess != a:
        guess = int(input("Next guess? "))
        if guess == a:
            print("Correct! Congratulations! ")
        elif guess >= (a + 20) or guess <= (a - 20):
            print("Not even close!")
        elif (guess >= (a + 10) or guess <= (a - 10)) and (guess < (a + 20) or guess > (a - 20)):
            print("Getting there...")
        elif (guess >= (a + 5) or guess <= (a - 5)) and (guess < (a + 10) or guess > (a - 10)):
            print("Almost there!")
        elif guess <= (a + 5) or guess >= (a - 5):
                print("Very close!")

main()