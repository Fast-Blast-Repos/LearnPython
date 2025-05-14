# Difficulty: 2/5

def mistery(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

print(mistery(5))
print(mistery(7))