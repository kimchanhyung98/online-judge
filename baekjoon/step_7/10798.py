words = [input() for _ in range(5)]

length = max(len(word) for word in words)
result = ''
for col in range(length):
    for row in range(5):
        if col < len(words[row]):
            result += words[row][col]

print(result)
