
with open('input.txt', 'r') as fin:
    data = [[int(number) for number in row] for row in fin.read().split('\n')]

solution_1 = 0
solution_2 = None
step = 1
while True:
    flashed = set()
    for idx_r, r in enumerate(data):
        for idx_c, c in enumerate(r):
            q = [(idx_r, idx_c)]
            while q:
                rr, cc = q.pop()
                if 0 <= rr < 10 and 0 <= cc < 10 and (rr, cc) not in flashed:
                    data[rr][cc] += 1
                    if data[rr][cc] == 10:
                        data[rr][cc] = 0
                        flashed.add((rr, cc))
                        solution_1 += 1 if step <= 100 else 0
                        for i in [-1, 0, 1]:
                            for j in [-1, 0, 1]:
                                q.append((rr + i, cc + j))

    if len(flashed) == 100 and solution_2 is None:
        solution_2 = step
        break
    step += 1

print(solution_1)
print(solution_2)