import os

from util.input import read_string_list

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_string_list(filepath)

lines = []
for row in data:
    result, numbers = row.split(':')
    result = int(result)
    numbers = [int(x) for x in numbers.split()]
    lines.append((result, numbers))

solution_1 = 0
solution_2 = 0

for line_result, line_numbers in lines:

    queue = [(line_numbers[0], True)]
    for line_number in line_numbers[1:]:
        new_queue = []
        while queue:
            element, flag = queue.pop()
            new_queue.append((element + line_number, flag))
            new_queue.append((element * line_number, flag))
            new_queue.append((int(str(element) + str(line_number)), False))
        queue = new_queue
    if [target for target, flag in queue if target == line_result and flag is True]:
        solution_1 += line_result
    if [target for target, flag in queue if target == line_result]:
        solution_2 += line_result

print(solution_1)
print(solution_2)
