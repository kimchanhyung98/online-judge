word = input()

croatian_alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for alphabet in croatian_alphabets:
    word = word.replace(alphabet, '1')

print(len(word))
