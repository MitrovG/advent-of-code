import os

from util.input import read_full

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_full(filepath)

import re
mul_pattern = r'mul\(([0-9]{1,3}),([0-9]{1,3})\)'
do_pattern = r'do\(\)'
dont_pattern = r'don\'t\(\)'

mul_groups = re.finditer(mul_pattern, data)
do_groups = re.finditer(do_pattern, data)
dont_groups = re.finditer(dont_pattern, data)

do_range = [0]
for do_group in do_groups:
    do_range.append(do_group.start())
dont_range = [-1]
for dont_group in dont_groups:
    dont_range.append(dont_group.start())

solution1 = 0
solution2 = 0
for mul_group in mul_groups:
    x, y = mul_group.groups()
    value = int(x) * int(y)
    solution1 += value
    if max(p for p in dont_range if p < mul_group.start()) > max(p for p in do_range if p < mul_group.start()):
        continue
    solution2 += value

print(solution1)
print(solution2)
