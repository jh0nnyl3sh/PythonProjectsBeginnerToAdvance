# 1. Import Random
import random

# 2. Getting the User's Name and Greeting the User
name = input("What is your name: ")
print(f"Good Luck! {name}")

# 3. List of Words and Choosing a Random Word
words = [
    'rainbow', 'computer', 'science', 'programming', 'python',
    'mathematics', 'player', 'condition', 'reverse', 'water',
    'board', 'geeks'
    ]

word = random.choice(words)

# 4. Promting the User to Guess

print("\nGuess the characters")


# 5. Initializing Guesses and Truns
guesses = ''
turns = 12

# 6. The main game loop
# 6.1. Checking Each Character in the Word
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end= '')
        else:
            print("_")
            failed += 1
            
    # 6.2. Checking if the User Has Won
    if failed == 0:
        print("You Win")
        print(f"The word is: {word}")
        break
    
    # 6.3. Promting for the Next Guess
    guess = input("guess a character: ")
    guesses += 1
    
    # 6.4. Handling Incorrect Guesses
    if guess not in word:
        turns -= 1
        print("Wrong")
        print(f"You have {turns}, more guesses ")
        
    
