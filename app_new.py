import streamlit as st
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to set difficulty level
def set_difficulty(level):
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

# Function to check the guess
def check_answer(guess, answer, turns):
    if guess > answer:
        st.write('You have guessed too high!')
        return turns - 1
    elif guess < answer:
        st.write("You've guessed too low!")
        return turns - 1
    else:
        st.write(f"You got it right! The answer was {answer}. Hurrayyy!")
        return 0

# Streamlit app logic
def game():
    if 'turns' not in st.session_state:
        st.session_state.turns = None
        st.session_state.answer = None
        st.session_state.guess = None

    st.title('Number Guessing Game')
    st.subheader('I am thinking of a number between 1 to 100...')

    # Difficulty selection
    level = st.selectbox('Choose your difficulty level:', ['easy', 'hard'])

    if st.button('Start Game'):
        st.session_state.answer = randint(1, 100)
        st.session_state.turns = set_difficulty(level)
        st.session_state.guess = None
        st.write(f'Game started! You have {st.session_state.turns} guesses. Make your guess.')

    if st.session_state.turns is not None and st.session_state.guess is None:
        guess = st.number_input('Enter your guess:', min_value=1, max_value=100, step=1)

        if st.button('Check Guess'):
            if guess != st.session_state.answer:
                st.session_state.turns = check_answer(guess, st.session_state.answer, st.session_state.turns)
                if st.session_state.turns == 0:
                    st.write("You've run out of guesses. You lose!")
                    st.session_state.turns = None
                else:
                    st.write(f"You have {st.session_state.turns} attempts remaining.")
            else:
                st.write("Congratulations, you won!")
                st.session_state.turns = None  # Game over after correct guess

game()
