from art import logo, vs
from game_data import data
from replit import clear
import random


def game():
    """Run the game."""
    # Declaring score and conditional variable
    score = 0
    continue_game = True

    # Start the game loop
    while continue_game:
        # The clear() function below works at replit.com
        clear()
        print(logo)
        # Print the score it the person had already guessed right
        if score >= 1:
            print(f"You're right! Current score is {score}.")

        # Compare A
        if score == 0:
            celebrity_a = pick_celebrity()
            celebrity_a_index = celebrity_index(celebrity_a)
            data.pop(celebrity_a_index)
        letter = 'A'
        print_celebrity(letter, celebrity_a)

        # Print the vs
        print(vs)

        # Against B
        celebrity_b = pick_celebrity()
        while(celebrity_a == celebrity_b):
            celebrity_b = pick_celebrity()
        celebrity_b_index = celebrity_index(celebrity_b)
        data.pop(celebrity_b_index)
        letter = 'B'
        print_celebrity(letter, celebrity_b)

        # User choice
        user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
        
        # Get the correct answer for each situation
        right_answer = answer(user_choice, celebrity_a, celebrity_b)
        
        # Compare the answers and remove the celebrities to avoid repetition
        if user_choice == right_answer:
            score += 1
            if not data:
                print("You have won! You have reached the maximum score: 49!")
                continue_game = False
            else:
                if right_answer == 'B':
                    celebrity_a = celebrity_b
        else:
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            continue_game = False


# Generate a number to select a celebrity from the list
def pick_celebrity():
    """Pick an account from the data list."""
    selection = random.choice(data)
    return selection


# Print the letter and the celebrity details
def print_celebrity(letter, celebrity):
    """Format an account from the data list, so it can be printed."""
    print(f"Compare {letter}: {celebrity['name']}, {celebrity['description']} from {celebrity['country']}.")


# Return the correct answer, so it can be compared with the user's
def answer(choice, celebrity_A, celebrity_B):
    """Give us the correct answer, according to each situation."""
    if celebrity_A['follower_count'] > celebrity_B['follower_count']:
        right_answer = 'A'
    elif celebrity_A['follower_count'] < celebrity_B['follower_count']:
        right_answer = 'B'
    else:
        right_answer = choice
    return right_answer


# Get the index to, later, remove the celebrity from the list
def celebrity_index(celebrity):
    """Give us the index of the account picked from de list."""
    return data.index(celebrity)


# Game start
game()