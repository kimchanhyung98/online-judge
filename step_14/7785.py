n = int(input())
current_employees = set()

for _ in range(n):
    name, action = input().split()
    if action == "enter":
        current_employees.add(name)
    else:
        current_employees.remove(name)

for employee in sorted(current_employees, reverse=True):
    print(employee)
