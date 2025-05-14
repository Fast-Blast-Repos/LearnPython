# Difficulty: 1/5

def mistery(word1, word2):
    word1 = word1.lower()
    chars1 = list(word1)
    word2 = word2.lower()
    chars2 = list(word2)
    chars1.sort()
    chars2.sort()
    if chars1 == chars2:
        return True
    else:
        return False

print(mistery("listen", "silent"))
print(mistery("hello", "world"))
