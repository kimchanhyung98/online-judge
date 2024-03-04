n = int(input())

wheel = 1
rooms = 1
if n > 1:
    while rooms < n:
        rooms += 6 * wheel
        wheel += 1

print(wheel)
