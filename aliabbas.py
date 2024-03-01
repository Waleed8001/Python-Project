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
        guess = st.text_input("Enter your guess:")

        if st.button("Submit Guess" + str(attempts)):
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
