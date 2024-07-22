import sys


def is_valid_parenthesis_string(ps):
    stack = []
    for char in ps:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                return "NO"
    return "YES" if not stack else "NO"


data = sys.stdin.read().split()
t = int(data[0])
results = []
for i in range(1, t + 1):
    ps = data[i]  # parenthesis_string
    results.append(is_valid_parenthesis_string(ps))

sys.stdout.write("\n".join(results) + "\n")
