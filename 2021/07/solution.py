
with open('input.txt', 'r') as fin:
    data = list(map(int, fin.read().split(',')))

solution_1 = None
solution_2 = None
for idx in range(min(data), max(data) + 1):
    cost_1 = sum([abs(x - idx) for x in data])
    cost_2 = sum([int(abs(x - idx) * (abs(x - idx) + 1) / 2) for x in data])
    if solution_1 is None or cost_1 < solution_1:
        solution_1 = cost_1
    if solution_2 is None or cost_2 < solution_2:
        solution_2 = cost_2

print(solution_1)
print(solution_2)