n = int(input())

words = []
for _ in range(n):
    word = input()
    words.append(word)

unique_words = list(set(words))
sorted_words = sorted(unique_words, key=lambda x: (len(x), x))
for word in sorted_words:
    print(word)
