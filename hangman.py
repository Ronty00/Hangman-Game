import random
from nltk.corpus import words, wordnet as wn
from colorama import Fore, Style, init

# Initialize colorama for colored output
init(autoreset=True)

# Ensure you have downloaded the required datasets from NLTK
try:
    nltk.data.find("corpora/words.zip")
    nltk.data.find("corpora/wordnet.zip")
except:
    import nltk
    nltk.download("words")
    nltk.download("wordnet")
    nltk.download("omw-1.4")

# Get the list of English words
WORD_LIST = words.words()

# ASCII art for the hangman
HANGMAN_PICS = [
    """
      -----
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """,
]


def get_random_word():
    """Fetch a random English word."""
    word = random.choice(WORD_LIST)
    return word.lower()


def get_word_clue(word):
    """Fetch a clue (definition) for the word using WordNet."""
    synsets = wn.synsets(word)
    if synsets:
        # Get the definition of the first synset
        return synsets[0].definition()
    return "No clue available for this word."


def display_hangman(attempts):
    """Display the current state of the hangman."""
    print(Fore.RED + HANGMAN_PICS[attempts])


def hangman_game():
    """Main function to play the Hangman game."""
    print(Fore.CYAN + Style.BRIGHT + "Welcome to Hangman!")

    # Fetch a random word
    word_to_guess = get_random_word()

    # Fetch a clue for the word
    clue = get_word_clue(word_to_guess)

    guessed_word = ["_"] * len(word_to_guess)
    attempts = 0
    max_attempts = len(HANGMAN_PICS) - 1
    guessed_letters = set()

    print(Fore.YELLOW + f"\nClue: {clue}")

    while attempts < max_attempts:
        print("\n" + Fore.GREEN + " ".join(guessed_word))
        display_hangman(attempts)
        print(Fore.MAGENTA + f"Guessed Letters: {', '.join(sorted(guessed_letters))}")
        print(Fore.BLUE + f"Remaining Attempts: {max_attempts - attempts}")

        guess = input(Fore.CYAN + "Guess a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print(Fore.RED + "Please enter a single valid letter.")
            continue

        # Check if the letter was already guessed
        if guess in guessed_letters:
            print(Fore.RED + "You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        # Check if the guess is correct
        if guess in word_to_guess:
            print(Fore.GREEN + f"Good guess! '{guess}' is in the word.")
            for idx, char in enumerate(word_to_guess):
                if char == guess:
                    guessed_word[idx] = char
        else:
            print(Fore.RED + f"Oops! '{guess}' is not in the word.")
            attempts += 1

        # Check if the player has guessed the word
        if "_" not in guessed_word:
            print("\n" + Fore.GREEN + Style.BRIGHT + "Congratulations! You've guessed the word!")
            print(Fore.YELLOW + f"The word was: {word_to_guess}")
            break
    else:
        print("\n" + Fore.RED + Style.BRIGHT + "You've run out of attempts!")
        display_hangman(attempts)
        print(Fore.YELLOW + f"The word was: {word_to_guess}")
        print(Fore.CYAN + "Better luck next time!")


# Run the game
if __name__ == "__main__":
    hangman_game()





