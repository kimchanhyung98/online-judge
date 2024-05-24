word = input().upper()

alphabet_list = list(set(word))
count_list = []
for i in alphabet_list:
    alphabet_count = word.count(i)
    count_list.append(alphabet_count)

if count_list.count(max(count_list)) > 1:
    print('?')
else:
    print(alphabet_list[count_list.index(max(count_list))])
