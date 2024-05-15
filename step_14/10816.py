n = int(input())
cards = list(map(int, input().split()))

card_count = {}
for card in cards:
    if card in card_count:
        card_count[card] += 1
    else:
        card_count[card] = 1

m = int(input())
numbers = list(map(int, input().split()))

for number in numbers:
    if number in card_count:
        print(card_count[number], end=' ')
    else:
        print(0, end=' ')
