from numpy import prod

with open('input.txt', 'r') as fin:
    data = [[int(number) for number in row] for row in fin.read().split('\n')]

basin_data = [row[:] for row in data]


def find_basin(data, idx_r, idx_c):
    basin = 0
    q = [(idx_r, idx_c)]
    while q:
        r, c = q.pop(0)
        if 0 <= r < len(data) and 0 <= c < len(data[r]):
            up = data[r - 1][c] if r > 0 else 9
            down = data[r + 1][c] if r < len(data) - 1 else 9
            left = data[r][c - 1] if c > 0 else 9
            right = data[r][c + 1] if c < len(data[r]) - 1 else 9
            if data[r][c] != 9 and data[r][c] <= min(up, down, right, left):
                basin += 1
                data[r][c] = 9
                q.extend([(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)])

    return basin


solution_1 = 0
basins = []
for idx_r, row in enumerate(data):
    for idx_c, column in enumerate(row):
        up = data[idx_r - 1][idx_c] if idx_r > 0 else 9
        down = data[idx_r + 1][idx_c] if idx_r < len(data) - 1 else 9
        left = data[idx_r][idx_c - 1] if idx_c > 0 else 9
        right = data[idx_r][idx_c + 1] if idx_c < len(row) - 1 else 9
        if column < min(up, down, left, right):
            solution_1 += (column + 1)
            basin_len = find_basin(basin_data, idx_r, idx_c)
            basins.append(basin_len)

solution_2 = prod(sorted(basins, reverse=True)[:3])

print(solution_1)
print(solution_2)
