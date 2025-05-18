import random

p1 = [
    """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """,
    """
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    """,
    """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """
]
# mirrored p1
p2 = ["""
      _______
     (____   '---
    (_____)
    (_____)
     (____)
      (___)__.---
    """,
    """
           _______
      ____(____   '---
     (______
    (_______
     (_______
       (__________.---
    """,
    """
           _______
      ____(____   '---
     (______
    (__________
          (____)
           (___)__.---
    """]

Input = input("Rock, Paper, Scissors? (r/p/s): ").lower()
if Input == "r":
    print(p1[0])
    opponent = random.randint(0, 2)
    print(p2[opponent])
    if opponent == 0:
        print("It's a tie!")
    elif opponent == 1:
        print("You lose!")
    else:
        print("You win!")
elif Input == "p":
    print(p1[1])
    opponent = random.randint(0, 2)
    print(p2[opponent])
    if opponent == 0:
        print("You win!")
    elif opponent == 1:
        print("It's a tie!")
    else:
        print("You lose!")
elif Input == "s":
    print(p1[2])
    opponent = random.randint(0, 2)
    print(p2[opponent])
    if opponent == 0:
        print("You lose!")
    elif opponent == 1:
        print("You win!")
    else:
        print("It's a tie!")
else:
    print("Invalid input! Please enter 'r', 'p', or 's'.")