# Difficulty: 3/5

def mistery(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - shift_base - shift) % 26 + shift_base))
        else:
            result.append(char)
    return ''.join(result)

print(mistery("hello world", 0))
print(mistery("ifmmp xpsme", 1))
print(mistery("jgnnq yqtnf", 2))