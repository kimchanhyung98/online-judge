s = input()

alphabet = list(range(97, 123))
for i in range(len(alphabet)):
    print(s.find(chr(alphabet[i])), end=' ')
