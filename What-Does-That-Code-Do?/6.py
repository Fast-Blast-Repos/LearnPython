# Difficulty: 1/5

def mistery(word, text):
    text = text.lower().split()
    word = word.lower()
    count = 0
    for x in text:
        if word == x:
            count += 1
    return count

print(mistery('hello', 'Hello World'))
print(mistery('she', 'Supported neglected met she therefore unwilling discovery remainder. Way sentiments two indulgence uncommonly own. Diminution to frequently sentiments he connection continuing indulgence. An my exquisite conveying up defective. Shameless see the tolerably how continued. She enable men twenty elinor points appear. Whose merry ten yet was men seven ought balls.'))