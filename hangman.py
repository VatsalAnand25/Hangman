import random

def select_word(word_list):
    """
    Randomly selects and returns a word from the provided list.
    :param word_list: List of words to choose from.
    :return: A randomly selected word.
    """
    return random.choice(word_list)

def handle_guess(word, guessed_letters, guess):
    """
    Checks if the guessed letter is in the word and updates the guessed letters set.
    :param word: The word being guessed.
    :param guessed_letters: A set of letters guessed so far.
    :param guess: The current letter guessed by the player.
    :return: True if the guess is correct, False otherwise.
    """
    if guess in word:
        guessed_letters.add(guess)
        return True
    return False

def display_hangman(attempts):
    """
    Displays the hangman state based on the number of incorrect attempts.
    :param attempts: The number of incorrect guesses.
    """
    stages = [
        """
           --------
           |      |
           |      
           |      
           |      
           |      
        ---------
        """,
        """
           --------
           |      |
           |      O
           |      
           |      
           |      
        ---------
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      
           |      
        ---------
        """,
        """
           --------
           |      |
           |      O
           |     /|
           |      
           |      
        ---------
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |      
           |      
        ---------
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / 
           |      
        ---------
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / \\
           |      
        ---------
        """
    ]
    print(stages[attempts])

def display_game_state(word, guessed_letters, incorrect_guesses):
    """
    Displays the current state of the game, including correctly guessed letters,
    underscores for unguessed letters, and incorrect guesses.
    :param word: The word being guessed.
    :param guessed_letters: A set of correctly guessed letters.
    :param incorrect_guesses: A list of incorrect guesses.
    """
    displayed_word = ' '.join([letter if letter in guessed_letters else '_' for letter in word])
    print(f"\nWord: {displayed_word}")
    print(f"Incorrect guesses: {', '.join(incorrect_guesses)}")
    display_hangman(len(incorrect_guesses))

def main():
    """
    Main function to control the Hangman game flow.
    """
    # Predefined list of words
    word_list = ["python", "hangman", "challenge", "programming", "developer"]

    # Initialize game state
    word_to_guess = select_word(word_list)
    guessed_letters = set()
    incorrect_guesses = []
    max_attempts = 6

    print("Welcome to Hangman! Try to guess the word one letter at a time.")

    # Game loop
    while len(incorrect_guesses) < max_attempts and set(word_to_guess) != guessed_letters:
        display_game_state(word_to_guess, guessed_letters, incorrect_guesses)
        guess = input("Enter your guess (a single letter): ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters or guess in incorrect_guesses:
            print("You already guessed that letter. Try again.")
            continue

        # Check the guess
        if handle_guess(word_to_guess, guessed_letters, guess):
            print(f"Good job! {guess} is in the word.")
        else:
            incorrect_guesses.append(guess)
            print(f"Sorry, {guess} is not in the word.")

    # End of game
    if set(word_to_guess) == guessed_letters:
        print(f"\nCongratulations! You guessed the word: {word_to_guess}")
    else:
        display_game_state(word_to_guess, guessed_letters, incorrect_guesses)
        print(f"\nGame over! The word was: {word_to_guess}")

if __name__ == "__main__":
    main()
