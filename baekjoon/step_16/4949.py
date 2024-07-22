import sys


def is_balanced_string(s):
    stack = []
    for char in s:
        if char in "([":
            stack.append(char)
        elif char == ")":
            if not stack or stack[-1] != "(":
                return "no"
            stack.pop()
        elif char == "]":
            if not stack or stack[-1] != "[":
                return "no"
            stack.pop()
    return "yes" if not stack else "no"


data = sys.stdin.read().splitlines()
results = []
for line in data:
    if line == ".":
        break
    results.append(is_balanced_string(line))

for result in results:
    print(result)
