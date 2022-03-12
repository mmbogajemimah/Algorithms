
input_x = int(input("Please think of a number between 0 and 100! "))

low = 0
high = 100
guess = (low + high)//2

while abs(guess - input_x) > 0.1:
    print("Is your secret number {}?".format(str(guess)))
    response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if response == ("h"):
        high = guess
    elif response == ("l"):
        low = guess
    elif response == ("c"):
        print("Game over. Your secret number was: {}".format(str(guess)))
        break
    elif response != "h" or response != "l" or response !="c":
        print("Sorry, I did not understand your input.")
    guess = (low + high)/2.0


    