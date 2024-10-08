from mimetypes import guess_type
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Function to check users' guess against actual answer
def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns the number of turns remaining."""
    if user_guess > actual_answer:
        print("Too High.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too Low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")

#Function to set difficulty
def set_difficulty():
    level = input("choose a difficulty type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    # Choosing a random nuber between 1 to 100
    print("Welcome to the number Guessing Game!")
    print("I' m thinking of a number between 1 and 100")
    answer = randint(1,100)
    print(f"passt, the correct answer is{answer}")

    turns = set_difficulty()


    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let the user guess a number
        guess = int(input("Make a guess: "))
        # Track the number of turns and reduce by 1 if they get it wrong
        turns = check_answer(guess,answer,turns)
        if turns == 0:
            print("You've run out of guess, you lose.")
            return
        elif guess != answer:
            print("Guess again")

game()



# Repeat the guessing functionality if they get it wrong

#################################################
# choose_level = input("choose a difficulty type 'easy' or 'hard'").lower()
# if choose_level == 'easy':
#     for i in reversed(range(1,10)):
#         print(f"You have {i} attempts remaining to guess the number.")
#         Guess_number = int(input("Make a guess:"))
#         if Guess_number == random_number:
#             print(f"You got it! The answer was {Guess_number}")
#         elif Guess_number < random_number:
#             print("Too Low")
#         elif Guess_number > random_number:
#             print("Too High")
#         else:
#             print("You've run out of guesses, you lose.")
# def hard():
#     for i in reversed(range(1, 6)):
#         print(f"You have {i} attempts remaining to guess the number.")
#         Guess_number = int(input("Make a guess:"))
#         if Guess_number > random_number:
#             print("Too High")
#         elif Guess_number < random_number:
#             print("Too Low")
#         elif Guess_number == random_number:
#             print(f"You got it! The answer was {Guess_number}")
#         else:
#             print("You've run out of guesses, you lose.")
#
#
