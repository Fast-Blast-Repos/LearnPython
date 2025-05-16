import random # random library: Tutorials/Libraries/random.md

# setup min and max
min = int(input("Minimum:\n"))
max = int(input("Maximum:\n"))
# chose a random number
number = random.randint(min, max)

guess = number + 1 # makes sure guess is not equal to number

# main game loop
while guess != number:
    guess = int(input(f"Guess a number between {min} and {max}:\n")) # input guess
    # check if guess is too high or too low
    if guess < number:
        print("Guess higher.")
    elif guess > number:
        print("Guess lower.")

# if guess is correct
print(f"You got it right: {number}")