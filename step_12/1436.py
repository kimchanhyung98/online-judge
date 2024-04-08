n = int(input())

num = 666
count = 1
while True:
    if '666' in str(num):
        if count == n:
            print(num)
            break
        count += 1
    num += 1
