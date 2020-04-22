"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


# compares the current_score to the high_score
def score_compare(current_score, high_score):
    if high_score == 0:
        return current_score
    elif high_score > 0 and current_score < high_score:
        return current_score
    else:
        return high_score


# create a reset function for reset the answers and solutions
def reset(answer):
    del answer[:]
    start_game()


highScore = 0


# (function) Display Welcome message to the player
def welcome_message():
    print("""
    *########################################
    # Welcome to The Number Guessing Game   #
    *########################################  
    
    How to: Guess the number between 0 and 10
    The High Score is {}
    """.format(highScore))


def start_game():

    # write your code inside this function.
    welcome_message()

    # (list) (String) store a random number solution and store player's answers
    solution = int(random.randrange(0, 10))
    user_answers = []

    # continuously display the user to guess a number
    while True:
        try:

            user_input = int(input("Guess a number: "))
        except ValueError:
            print("Incorrect value, try again")
            continue

        user_answers.append(user_input)

        # the player can not add a number outside 0 - 10
        if user_input > 11 or user_input < 0:

            print("Please Guess between 0 to 10")
            continue

        # if answer is correct, display you have won with the amount of trys
        elif user_input == solution:

            # store high score and display it when player plays again
            print("You Won, Number of Guess {}".format(len(user_answers)))

            # the game is over, ask player want to start an new game
            user_option = input("Do you want to play again [Y] yes [N] No : ")

            if user_option.upper() == 'Y':
                global highScore
                highScore = score_compare(len(user_answers), highScore)
                reset(user_answers)

            else:
                print("Game over, thank you for playing")
                break

        # if the answer is wrong display either guess higher or lower
        elif user_input > solution:
            print("it's lower")
            continue

        elif user_input < solution:
            print("it's Higher")
            continue


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
