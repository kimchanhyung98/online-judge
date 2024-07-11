k = int(input().strip())
numbers = [int(input().strip()) for _ in range(k)]

stack = []
for number in numbers:
    if number == 0:  # if stack:
        stack.pop()
    else:
        stack.append(number)

print(sum(stack))
