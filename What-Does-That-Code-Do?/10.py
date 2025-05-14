# Difficulty: 2/5

def mistery(sentence):
    words = sentence.split()
    return ' '.join(words[::-1])

print(mistery("Hello world"))
print(mistery("Python is fun"))