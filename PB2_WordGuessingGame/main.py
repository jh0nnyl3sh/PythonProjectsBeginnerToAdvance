import random

name = input("What is your name: ")
print(f"Good Luck! {name}")

# List of Words and Choosing a Random Word
words = [
    'rainbow', 'computer', 'science', 'programming', 'python',
    'mathematics', 'player', 'condition', 'reverse', 'water',
    'board', 'geeks'
    ]

word = random.choice(words)

print("\nGuess the characters")


# Initializing Guesses and Truns
guesses = ''
turns = 12

# The main game loop
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end= '')
        else:
            print("_")
            failed += 1