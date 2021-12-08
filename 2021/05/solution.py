
with open('input.txt', 'r') as fin:
    data = fin.read().split('\n')

points = dict()
points_diag = dict()
for row in data:
    first, _, second = row.partition(' -> ')
    x1, y1 = map(int, first.split(','))
    x2, y2 = map(int, second.split(','))

    if x1 == x2:
        for idx in range(min(y1, y2), max(y1, y2) + 1):
            points.setdefault((x1, idx), 0)
            points[(x1, idx)] += 1
    elif y1 == y2:
        for idx in range(min(x1, x2), max(x1, x2) + 1):
            points.setdefault((idx, y1), 0)
            points[(idx, y1)] += 1
    else:
        for idx in range(abs(x2 - x1) + 1):
            x = x1 + idx if x2 > x1 else x1 - idx
            y = y1 + idx if y2 > y1 else y1 - idx
            points_diag.setdefault((x, y), 0)
            points_diag[(x, y)] += 1

points_full = {k: points.get(k, 0) + points_diag.get(k, 0) for k in set(points) | set(points_diag)}

solution_1 = len([x for x in points.values() if x > 1])
solution_2 = len([x for x in points_full.values() if x > 1])

print(solution_1)
print(solution_2)