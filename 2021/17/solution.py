import re

with open('input.txt', 'r') as fin:
    data = fin.read()

x_min, x_max, y_min, y_max = map(int, re.findall(r'-?\d+', data))

positions = list()
for x in range(x_max + 1):
    for y in range(y_min, -y_min):
        new_x = x
        new_y = y
        dx = x
        dy = y
        max_y = y_min

        while True:
            if new_x > x_max or new_y < y_min:
                break
            if x_min <= new_x <= x_max and y_min <= new_y <= y_max:
                positions.append(max_y)
                break
            if dx > 0:
                dx -= 1
            dy -= 1
            new_x += dx
            new_y += dy
            if new_y > max_y:
                max_y = new_y

solution_1 = max(positions)
solution_2 = len(positions)
print(solution_1)
print(solution_2)

# TODO: Try analytical
