print("Please think of a number between 0 and 100!")

low = 0
high = 100
guessed = False


while not guessed:
    guess = (low + high)//2
    print("Is your secret number {} ?".format(str(guess)))
    response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if response == "c":
        print("Game over. Your secret number was: {}".format(str(guess)))
        guessed = True
    elif response == "l":
        low = guess
    elif response == "h":
        high = guess
    elif response != "h" or response != "l" or response !="c":
        print("Sorry, I did not understand your input.")

