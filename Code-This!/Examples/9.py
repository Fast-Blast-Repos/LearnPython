# TY to deostroll for making the Scrabble word list: https://gist.github.com/deostroll/7693b6f3d48b44a89ee5f57bf750bd32

# Advanced Version:
# print("That word is allowed in Scrabble.") if input("Word: ").upper() in open("9.txt", "r").read().split() else print("That word is NOT allowed in Scrabble.")

with open("9.txt", "r") as file:
    words = file.read()
    words = words.split()

word = input("Word: ")
word = word.upper()
if word in words:
    print("That word is allowed in Scrabble.")
else:
    print("That word is NOT allowed in Scrabble.")