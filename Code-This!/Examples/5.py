import random

states = ["""______
|    |
|    O
|   /|\\
|   / \\
|_______
""","""______
|    |
|    O
|   /|\\
|   /
|_______
""","""______
|    |
|    O
|   /|\\
|   
|_______
""","""______
|    |
|    O
|   /|
|   
|_______
""","""______
|    |
|    O
|    |
|   
|_______
""","""______
|    |
|    O
|   
|   
|_______
""","""______
|    |
|    
| 
|  
|_______
"""]

with open("5.txt", "r") as file:
    words = file.read().splitlines()
word = random.choice(words)
guesses = 6
guessed = []

while guesses > 0:
    print(states[guesses])
    print("Word: ", end="")
    for letter in word:
        if letter in guessed:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("\nGuessed letters: ", end="")
    for letter in guessed:
        print(letter, end=" ")
    print("\nGuesses left: ", guesses)
    
    guess = input("Guess a letter: ").lower()
    
    if guess in guessed:
        print("You already guessed that letter!")
        continue
    
    guessed.append(guess)
    
    if guess not in word:
        guesses -= 1
        print("Wrong guess!")
    
    if all(letter in guessed for letter in word):
        print("Congratulations! You guessed the word:", word)
        break
else:
    print(states[guesses])
    print("You lost! The word was:", word)