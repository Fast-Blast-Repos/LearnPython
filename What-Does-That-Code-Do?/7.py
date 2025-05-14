# Difficulty: 2/5

import os

def mistery(path, extension):
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                count += 1
    return count

print(mistery('.', '.py'))
print(mistery('.', '.md'))