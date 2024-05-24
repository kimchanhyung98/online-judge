s = input()

substrings = set()
for start in range(len(s)):
    for length in range(1, len(s) - start + 1):
        substrings.add(s[start:start + length])

print(len(substrings))
