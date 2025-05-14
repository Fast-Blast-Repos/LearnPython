# Difficulty: 1/5

def mistery(num):
    if num == 0 or num == 1:
        return "Maybe"
    else:
        var = num % 2
        if var == 0:
            return True
        else:
            return False

print(mistery(1))
print(mistery(6))
print(mistery(3))