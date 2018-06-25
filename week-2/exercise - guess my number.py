"""In this problem, you'll create a program that guesses a secret number!

The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search, the computer will guess the user's secret number!

"""

low = 0
high = 100
guess = (low + high)//2
correct_guess = False

print("Please think of a number between " + str(low) + " and " + str(high) + "!")
# uses boolean to flag when correct guess has been marked
while correct_guess == False:
    print("Is your secret number " + str(guess) + "?")
    print("Enter 'h' to indicate the guess is too high.", end=" ")
    print("Enter 'l' to indicate the guess is too low", end=" ")
    print("Enter 'c' to indicate the guess is correct", end=" ")
    response = input()
    if response == "h":
        high = guess
        guess = (low + high)//2
    elif response == "l":
        low = guess
        guess = (low + high)//2
    elif response == "c":
        correct_guess = True
    else: # handle incorrect input
        print("Sorry I did not understand your input")

print("Game over", end=" ")
print("Your secret number was: ", end=" ")
print(guess)