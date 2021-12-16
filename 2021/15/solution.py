from collections import Counter

with open('input.txt', 'r') as fin:
    data = [[int(x) for x in y] for y in fin.read().split('\n')]

risk = Counter()
height = len(data)
width = len(data[0])

grid = []
for row in data:
    new_row = row[:]
    for i in range(1, 5):
        new_row.extend([(element + i) if (element + i) < 10 else (element + i - 9) for element in row])
    grid.append(new_row)


for i in range(1, 5):
    new_rows = []
    for j in range(height):
        row = [(element + i) if (element + i) < 10 else (element + i - 9) for element in grid[j]]
        new_rows.append(row)
    grid.extend(new_rows)

step = 0
while True:
    counter = 0
    step += 1
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if i == 0 and j == 0:
                risk[(i, j)] = 0
                continue
            up = risk.get((i-1, j), float('inf'))
            left = risk.get((i, j-1), float('inf'))
            down = risk.get((i+1, j), float('inf'))
            right = risk.get((i, j+1), float('inf'))
            new_value = grid[i][j] + min(up, left, right, down)
            if new_value != risk[i, j]:
                counter += 1
            risk[i, j] = new_value
    if counter == 0:
        break
    print('Step:', step, 'Elements to be fixed:', counter)

print(risk[(height-1, width-1)])
print(risk[(height * 5 - 1, width * 5 - 1)])

# FIXME: Bad solution (Forgot about going up and left, so I just added a loop) - Use Djikstra
