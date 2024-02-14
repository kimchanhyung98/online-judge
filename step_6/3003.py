pieces = list(map(int, input().split()))

correct_pieces = [1, 1, 2, 2, 2, 8]
for i in range(len(pieces)):
    print(correct_pieces[i] - pieces[i], end=" ")
