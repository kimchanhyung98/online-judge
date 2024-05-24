n = int(input())

members = []
for i in range(n):
    age, name = input().split()
    members.append((int(age), i, name))

for member in sorted(members):
    print(member[0], member[2])
