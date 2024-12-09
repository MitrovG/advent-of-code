import os

from util.input import read_full

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_full(filepath)

free = []
full = []
disk_map = []
flag = True
counter = 0
position = 0
for element in data:
    element = int(element)
    if flag:
        disk_map.extend([counter] * element)
        full.append((counter, position, element))
        position += element
        counter += 1
    else:
        disk_map.extend([-1] * element)
        free.append((element, position))
        position += element
    flag = not flag

# Part 1
i = 0
j = len(disk_map) - 1
while i < j:
    if disk_map[i] != -1:
        i += 1
    elif disk_map[j] == -1:
        j -= 1
    else:
        disk_map[i], disk_map[j] = disk_map[j], disk_map[i]
        i += 1
        j -= 1
solution_1 = 0
for i, element in enumerate(disk_map):
    if element != -1:
        solution_1 += i*element
print(solution_1)

# Part 2
new_order = []
for file in full[::-1]:
    value, start, size = file
    for idx, (size_f, position_f) in enumerate(free):
        if start <= position_f:
            new_order.append((value, start, start + size))
            break
        if size <= size_f:
            new_order.append((value, position_f, position_f + size))
            free[idx] = (size_f - size, position_f + size)
            break
    else:
        new_order.append((value, start, start + size))

solution_2 = 0
for element, start, end in new_order:
    while start < end:
        solution_2 += element * start
        start += 1
print(solution_2)
