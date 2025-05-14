# Difficulty: 2/5

def mistery(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

print(mistery(1))
print(mistery(9))
print(mistery(13))