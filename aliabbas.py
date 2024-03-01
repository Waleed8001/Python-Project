import streamlit as st
import requests

# Function to fetch a random word from an API
def fetch_random_word():
    response = requests.get("https://api.example.com/random_word")
    if response.status_code == 200:
        return response.json().get("word")
    else:
        return None

# Main function to run the game
def word_guessing_game():
    st.title("Word Guessing Game")
    st.write("Try to guess the word!")

    # Fetch a random word from the API
    word = fetch_random_word()
    if not word:
        st.error("Failed to fetch word from API. Please try again later.")
        return

    # Display placeholders for letters in the word
    guessed_word = ["_" for _ in word]
    st.write(" ".join(guessed_word))

    # Game loop
    attempts = 0
    while "_" in guessed_word:
        guess = st.text_input("Enter a letter:")
        if len(guess) == 1:
            if guess in word:
                for i, letter in enumerate(word):
                    if letter == guess:
                        guessed_word[i] = guess
                st.write(" ".join(guessed_word))
            else:
                st.write("Incorrect guess.")
                attempts += 1
        else:
            st.write("Please enter only one letter.")

    st.success(f"Congratulations! You guessed the word '{word}' in {attempts} attempts.")

# Run the game
word_guessing_game()
