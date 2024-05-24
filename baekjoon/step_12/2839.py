n = int(input())

bag_5kg = n // 5
remainder = n % 5
while bag_5kg >= 0:
    if remainder % 3 == 0:
        bag_3kg = remainder // 3
        print(bag_5kg + bag_3kg)
        break

    bag_5kg -= 1
    remainder += 5
else:
    print(-1)
