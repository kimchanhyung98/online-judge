import sys

n, m = map(int, sys.stdin.readline().split())

pokemon_name = {}
pokemon_number = {}
for i in range(1, n + 1):
    name = sys.stdin.readline().strip()
    pokemon_name[i] = name
    pokemon_number[name] = i

for _ in range(m):
    problem = sys.stdin.readline().strip()
    if problem.isdigit():
        print(pokemon_name[int(problem)])
    else:
        print(pokemon_number[problem])
