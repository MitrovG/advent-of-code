import os
from collections import Counter

import numpy

from util.input import read_string_parts

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_string_parts(filepath)

# Parse input
monkeys = [dict() for _ in range(8)]
for monkey_data in data:
    monkey_data = monkey_data.split('\n')
    monkey_id = int(monkey_data[0][-2])

    worries = monkey_data[1].split(':')[1].split(',')
    worries = list(map(int, worries))
    monkeys[monkey_id]['worries'] = worries

    operation = monkey_data[2].split('=')[1].strip()
    monkeys[monkey_id]['op'] = operation
    test = int(monkey_data[3].split('by ')[1])
    monkeys[monkey_id]['test'] = test

    if_true = int(monkey_data[4].split('monkey ')[1])
    if_false = int(monkey_data[5].split('monkey ')[1])
    monkeys[monkey_id]['true'] = if_true
    monkeys[monkey_id]['false'] = if_false

part_2_modulo = numpy.prod([monkey['test'] for monkey in monkeys])
part_1_range = 21
part_2_range = 10_001

inspections = Counter()
for round in range(1, part_2_range):
    for idx_m, monkey in enumerate(monkeys):
        while monkey['worries']:
            worry = monkey['worries'].pop(0)
            inspections[idx_m] += 1
            operation = monkey['op'].replace('old', str(worry))
            new_worry = eval(operation)
            # part 1
            # new_worry = new_worry // 3
            # part 2
            new_worry = new_worry % part_2_modulo
            if new_worry % monkey['test'] == 0:
                monkeys[monkey['true']]['worries'].append(new_worry)
            else:
                monkeys[monkey['false']]['worries'].append(new_worry)

result = inspections.most_common(2)
solution_1 = result[0][1] * result[1][1]
print(solution_1)
