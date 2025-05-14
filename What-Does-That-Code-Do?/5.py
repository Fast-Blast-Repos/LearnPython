# Difficulty: 3/5

def mistery(Offset, Text):
    Text = Text.lower()
    Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    ShiftedAlphabet = Alphabet[Offset:] + Alphabet[:Offset]
    Table = str.maketrans(''.join(Alphabet), ''.join(ShiftedAlphabet))
    return Text.translate(Table)

print(mistery(0, 'Hello World'))
print(mistery(1, 'Hello World'))
print(mistery(2, 'Hello World'))