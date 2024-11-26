from random import randint
from art import logo

EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5

def set_difficulty():
    level=input("Choose your dificulty level: ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
    

def check_answer(guess,answer,turns):
    if guess > answer:
        print('You have guessed too high')
        return turns-1
    elif guess < answer:
        print("You've guessed too low")
        return turns-1
    else:
        print(f"You got it right. The answer was {answer}. Hurrayyy!")



def game():
    print(logo)
    print('Welcome to the Number Guessing Game.')
    print('I am thinking of a number between 1 to 100...')
    answer = randint(1,100)
    guess=0

    turns=set_difficulty()
    while guess!=answer:
        print("**********************************************************************")
        print(f"\nYou have {turns} attempts remaining")
        guess=int(input('Guess a number: '))
        turns=check_answer(guess,answer,turns)

        if turns==0:
            print("You've run out of guesses. You lose ")
            return
        elif guess!=answer:
            print("Guess Again")

game()