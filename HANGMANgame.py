#Project_1: HANGMAN_GAME
import random

#RULES:
"""
1:The goal is to guess a hidden word, one letter at a time.
2:For each correct guess, the letter is filled in the corresponding dash.
3:For each incorrect guess, a part of a stick figure is drawn, representing a man being "hanged". The figure is drawn in stages (head, body, arms, legs, etc.).
4:The game continues until the word is completely guessed or the stick figure is fully drawn, resulting in a loss.
5:The player haas 7 tries to guess the word
"""

def choose_word():
    # List of possible words
    words = ['python','hangman','programming','engineer','project','internship','placement','college','school']
    return random.choice(words)

def display_hangman(tries):
    stages = ["""
                --------
                |      |
                |      O
                |     \|/
                |      |
                |     / \
                -
             """,
             """
                --------
                |      |
                |      O
                |     \|/
                |      |
                |     / 
                -
             """,
             """
                --------
                |      |
                |      O
                |     \|/
                |      |
                |      
                -
             """,
             """
                --------
                |      |
                |      O
                |     \|/
                |      
                |     
                -
             """,
             """
                --------
                |      |
                |      O
                |      |/   
                |      
                |     
                -
             """,
             """
                --------
                |      |
                |      O
                |      |
                |      
                |     
                -
             """,
             """
                --------
                |      |
                |      O
                |    
                |      
                |     
                -
             """,
             """
                --------
                |      |
                |      
                |    
                |      
                |     
                -
             """
    ]
    return stages[tries]

def play_hangman():
    word = choose_word()
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 7

    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed the letter {guess}")
            elif guess not in word:
                print(f"{guess} is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"Good job! {guess} is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"You already guessed the word {guess}")
            elif guess != word:
                print(f"{guess} is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    
    if guessed:
        print("Congratulations, you guessed the word! You win!")
    else:
        print(f"Sorry, you ran out of tries. The word was {word}. Better luck next time!")

# Start the game
play_hangman()
