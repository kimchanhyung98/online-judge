n = int(input())
arr = list(map(int, input().split()))

sorted_arr = sorted(set(arr))
compression_dict = {value: index for index, value in enumerate(sorted_arr)}
print(*[compression_dict[value] for value in arr])
