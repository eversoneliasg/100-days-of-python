from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")

number_chosen = random.randint(0,100)

print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty! Type 'easy' or hard': ").lower()

if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5
else:
    print("Ok, I think you don't wanna play. Bye bye!")
    attempts = 0

guessed_wrong = True

while attempts > 0 and guessed_wrong:
    print(f"You have {attempts} attempts remaining to guess the number!")
    guess = int(input("Make a guess: "))
    if guess > number_chosen:
        if attempts > 1:
            print("Too high.\nGuess again.")
            attempts -= 1
        else:
            attempts -= 1
    elif guess < number_chosen:
        if attempts > 1:
            print("Too low.\nGuess again.")
            attempts -= 1
        else:
            attempts -= 1
    else:
        guessed_wrong = False

if attempts > 0 and not guessed_wrong:
    print(f"You got it! The answer was {number_chosen}.")
else:
    print(f"You've run out of guesses! The answer was {number_chosen}. You lose!")
