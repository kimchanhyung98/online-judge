total_price = int(input())
items = int(input())

calculated_price = 0
for _ in range(items):
    price, item = map(int, input().split())
    calculated_price += price * item

print("Yes" if calculated_price == total_price else "No")
