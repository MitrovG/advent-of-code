import os

from util.input import read_string_list

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_string_list(filepath)

cycles = (20, 60, 100, 140, 180, 220)
cycle = 0
register = 1
results = []
crt_index = 0


def increment_cycle(cycle: int):

    global crt_index
    cycle += 1
    if cycle in cycles:
        results.append(cycle * register)

    if crt_index in (register - 1, register, register + 1):
        print('#', end='')
    else:
        print('.', end='')
    crt_index = (crt_index + 1) % 40
    if crt_index == 0:
        print()

    return cycle


for instruction in data:

    if instruction == 'noop':
        cycle = increment_cycle(cycle)
    elif instruction.startswith('addx'):
        add_to_register = int(instruction.split()[-1])
        cycle = increment_cycle(cycle)
        cycle = increment_cycle(cycle)
        register += add_to_register

solution_1 = sum(results)
print(solution_1)
