Hangman is a classic word-guessing game. Its origins are not exactly known but it appears to date back to Victorian times. A player writes down the first and last letters of a word, and another player guesses the letters in between.

This article will show you how to create a simple Hangman game in Python. This is a great beginner project to practice programming logic and handling strings, loops, and conditions.

How the Game Works
The program randomly selects a word from a list of secret words.
The player has limited chances to guess the word.
When a correct letter is guessed, it is revealed in its correct position.
The player wins if all letters are guessed before running out of chances.
For simplicity, the program gives word length + 2 chances.
Example: If the secret word is mango (5 letters), the player gets 7 chances.

Explanation:

someWords.split(' '): Converts the string of words into a list.
word = random.choice(someWords): Selects a random secret word for the game.
chances = len(word) + 2: Sets number of chances based on word length.
guess = input(...).lower(): Takes a single letter input from the player.
if not guess.isalpha() ... Validates the input for letters only and uniqueness.
letterGuessed += guess * word.count(guess): Adds correctly guessed letters to the guessed list.
if chances <= 0 ... Ends the game if the player runs out of chances.
Try it yourself Exercises: 
You can further enhance program by adding timer after every Guess
You can also give hints from the beginning to make the task a bit easier for user
You can also decrease the chance by one only if the player's guess is WRONG. If the guess is right, 
player's chance is not reduced.

https://www.geeksforgeeks.org/python/hangman-game-python/