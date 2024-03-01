import streamlit as st
import random

def number_guessing_game():
    st.title("Number Guessing Game")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    # Initialize variables
    guess = None
    attempts = 0

    st.write("I have selected a number between 1 and 100. Try to guess it!")

    # Main game loop
    while guess != secret_number:
        # User input for guessing with a unique key
        input_key = f'guess_input_{attempts}'
        guess = st.number_input("Enter your guess:", min_value=1, max_value=100, key=input_key)

        button_key = f'submit_button_{attempts}'
        if st.button(f"Submit Guess {attempts}", key=button_key):
            attempts += 1

            # Check if the guess is correct
            if guess == secret_number:
                st.success(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
            else:
                st.info(f"Wrong guess! Try again.")

    # Restart the game
    if st.button("Play Again"):
        number_guessing_game()

# Run the game
number_guessing_game()
