n, b = input().split()

result = 0
for digit, char in enumerate(n[::-1]):
    if char.isdigit():
        result += int(char) * (int(b) ** digit)
    else:
        result += (ord(char) - 55) * (int(b) ** digit)

print(result)
