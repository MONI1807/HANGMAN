import random
# Predefined list of 5 words for the Hangman game
WORDS = ["cloud", "virus", "robot", "cookie", "bug"]
# Predefined dictionary of words and their corresponding clues
WORD_DATABASE = {
    "cloud": "Stores file online,not in the sky.",
    "virus": "can affect both computers and living organisms.",
    "robot": "A machine that can perform tasks automatically.",
    "cookie": "Stored by websites,but also a sweet snack.",
    "bug": "Causes problems in code,but also an insert."
}
# ASCII art for the hangman stages corresponding to incorrect guesses (from 0 to 6)
HANGMAN_STAGES = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]
def get_word():
    """Selects and returns a random word from the predefined word list."""
    return random.choice(WORDS)
def display_rules():
    """Prints the game rules and instructions on how to play."""
    print("=" * 60)
    print("                    HOW TO PLAY & GAME RULES")
    print("=" * 60)
    print("1. The computer will pick a random secret word.")
    print("2. You will be given a clue about the word's meaning.")
    print("3. Guess the word by typing one letter at a time.")
    print("4. For every correct guess, the letter will be revealed in the word.")
    print("5. For every incorrect guess, a part of the hangman is drawn.")
    print("6. You have a maximum of 6 incorrect guesses before the game is over.")
    print("7. You can type 'exit' at any time to quit the game.")
    print("=" * 60)
    input("Press Enter to start the game...")
def display_game_state(secret_word, clue, guessed_letters, incorrect_guesses):
    """
    Displays the current hangman figure, the secret word with blank spots, 
    and the list of guessed letters.
    Displays the current hangman figure, the clue, the secret word with 
    blank spots, and the list of guessed letters.
    """
    # Print the current hangman ASCII art stage based on incorrect guesses
    print(HANGMAN_STAGES[incorrect_guesses])
    print(f"💡 CLUE: {clue}")
    
    # Display the word with underscores for unguessed letters
    displayed_word = [letter if letter in guessed_letters else "_" for letter in secret_word]
    print(f"Word: {' '.join(displayed_word)}")
    
    # Display incorrect guesses remaining and letters guessed so far
    print(f"Incorrect guesses remaining: {6 - incorrect_guesses} / 6")
    if guessed_letters:
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
    print("-" * 30)
    print("-" * 50)
def get_valid_guess(guessed_letters):
    """
    Prompts the user to enter a single letter and validates the input.
    Allows the user to type 'exit' to quit.
    """
    while True:
        guess = input("Enter a letter (or 'exit' to quit): ").strip().lower()
        
        # Check for exit command
        if guess == 'exit':
            return 'exit'
            
        # Validation checks
        if len(guess) != 1:
            print("❌ Invalid input! Please enter exactly one letter.")
        elif not guess.isalpha():
            print("❌ Invalid input! Please enter a letter (A-Z).")
        elif guess in guessed_letters:
            print(f"⚠️ You have already guessed '{guess}'. Try a different letter.")
        else:
            return guess
    """Executes a single complete round of Hangman."""
    secret_word = get_word()
def play_round(scores):
    """
    Executes a single complete round of Hangman.
    Updates the scores dictionary in-place.
    """
    # Select word and its clue
    secret_word = random.choice(list(WORD_DATABASE.keys()))
    clue = WORD_DATABASE[secret_word]
    
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    
    print("\n" + "="*40)
    print("      Welcome to Python Hangman!      ")
    print("="*40)
    print("\n" + "="*50)
    print("                 NEW ROUND STARTED")
    print("="*50)
    
    while incorrect_guesses < max_incorrect_guesses:
        display_game_state(secret_word, clue, guessed_letters, incorrect_guesses)
        
        # Get a valid, unique guess from the user
        guess = get_valid_guess(guessed_letters)
        
        if guess == 'exit':
            print("\nExiting current round...")
            return 'exit'
            
        guessed_letters.add(guess)
        
        # Process the guess
        if guess in secret_word:
            print(f"\n✅ Good guess! '{guess}' is in the word.")
            # Check if all letters in the secret word have been guessed
            if all(letter in guessed_letters for letter in secret_word):
                display_game_state(secret_word, clue, guessed_letters, incorrect_guesses)
                print(f"🎉 Congratulations! You guessed the word: '{secret_word.upper()}'! 🎉\n")
                scores["wins"] += 1
                return True
        else:
            incorrect_guesses += 1
            print(f"\n❌ Sorry, '{guess}' is not in the word.")
            
    # If we exited the loop, the player has run out of guesses
    print(HANGMAN_STAGES[incorrect_guesses])
    print(" Game Over! You ran out of guesses.")
    print(f"The word was: '{secret_word.upper()}'")
    print(f"Definition: {clue}\n")
    scores["losses"] += 1
    return False
def main():
    """Main game entry point that handles rules display, score tracking, and replay loop."""
    display_rules()
    
    # Persistent score tracking
    scores = {"wins": 0, "losses": 0}
    
    while True:
        result = play_round(scores)
        if result == 'exit':
            break
            
        # Display current scores
        print("=" * 30)
        print(f"🏆 CURRENT SCORE:")
        print(f"   Wins:   {scores['wins']}")
        print(f"   Losses: {scores['losses']}")
        print("=" * 30)
        
        # Replay prompt
        play_again = input("Would you like to play another round? (y/n): ").strip().lower()
        if play_again not in ('y', 'yes'):
            print("\nThanks for playing Hangman! Goodbye!")
            break
    print("\n" + "=" * 50)
    print(f"🏁 FINAL SCORE: Wins: {scores['wins']} | Losses: {scores['losses']}")
    print("Thanks for playing Hangman! Goodbye!")
    print("=" * 50)
if __name__ == "__main__":
    main()