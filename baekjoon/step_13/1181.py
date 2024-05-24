n = int(input())

words = []
for _ in range(n):
    word = input()
    words.append(word)

sorted_words = sorted(list(set(words)), key=lambda x: (len(x), x))
for word in sorted_words:
    print(word)
