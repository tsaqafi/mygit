# Generate a random number between 1 and 9.
# Ask the user to guess the numbe, then tell them guessed too low
# or high
import random
num = random.randint(1,9)
trial = 0
User = input(print("type 'exit' to quit or 'play' to play"))
guess_str = input(print("Guess a number between 1 to 9 "))
guess_int = int(guess_str)

while User != "exit":
    trial = trial + 1
    if guess_int == num:
        User = input(print("You guess the correct number, type 'exit' to quit"))
    elif guess_int > num:
        guess_int = int(input(print("The number you guess is higher, guess again ")))
    elif guess_int < num:
        guess_int = int(input(print("The number you guess is lower, guess again ")))
else:
    print("The number of trial to guess the number is", trial)