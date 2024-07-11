import sys

data = sys.stdin.read().split()
stack = []
results = []

index = 1
for _ in range(int(data[0])):
    if data[index] == '1':
        stack.append(data[index + 1])
        index += 2
    elif data[index] == '2':
        if stack:
            result = stack.pop()
            results.append(str(result))
        else:
            results.append("-1")
        index += 1
    elif data[index] == '3':
        results.append(str(len(stack)))
        index += 1
    elif data[index] == '4':
        result = "0" if stack else "1"
        results.append(result)
        index += 1
    elif data[index] == '5':
        if stack:
            result = stack[-1]
            results.append(str(result))
        else:
            results.append("-1")
        index += 1

sys.stdout.write("\n".join(results))
