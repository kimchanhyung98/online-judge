n = int(input())
numbers = list(map(int, input().split()))

count = 0
for num in numbers:
    if num <= 1:
        continue

    if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
        count += 1

print(count)
