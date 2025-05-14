# Difficulty: 1/5

def mistery(word):
    word = word.lower()
    chars = list(word)
    reversed = []
    for i in range(len(chars) - 1, -1, -1):
        reversed.append(chars[i])
    if chars == reversed:
        return True
    else:
        return False

print(mistery("Hello"))
print(mistery("Racecar"))