from __future__ import annotations
import os

from util.input import read_string_list

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_string_list(filepath)


def yell(monkey: str):
    value = monkeys[monkey]
    try:
        value = int(value)
        return value
    except ValueError:
        op = value.split()
        first = yell(op[0])
        second = yell(op[2])
        return eval(f"{first}{op[1]}{second}")


monkeys = dict()
for row in data:
    monkey, operation = row.split(':')
    operation = operation.strip()
    monkeys[monkey] = operation

solution_1 = int(yell('root'))
print(solution_1)
