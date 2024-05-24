dice = list(map(int, input().split()))

if len(set(dice)) == 1:
    prize = 10000 + dice[0] * 1000
elif len(set(dice)) == 2:
    prize = 1000 + (dice[0] if dice[0] == dice[1] else dice[2]) * 100
else:
    prize = max(dice) * 100

print(prize)
