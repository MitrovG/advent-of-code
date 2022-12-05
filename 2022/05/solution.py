import os
import re

from util.input import read_full

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_full(filepath)

supplies, instructions = data.split('\n\n')

supplies = supplies.split('\n')
crates = [[] for _ in range(10)]
for supply_row in supplies[:-1]:
    idx = 0
    crate_idx = 1
    while idx <= len(supply_row):
        crate_value = supply_row[idx+1: idx+2].strip()
        if crate_value:
            crates[crate_idx].insert(0, crate_value)
        crate_idx += 1
        idx += 4

pattern = re.compile(r'move ([0-9]*) from ([0-9]*) to ([0-9]*)')
for instruction in instructions.split('\n'):
    result = pattern.match(instruction)
    blocks = int(result.group(1))
    from_crate = int(result.group(2))
    to_crate = int(result.group(3))

    # for part 1
    # crates[to_crate].extend(reversed(crates[from_crate][-blocks:]))
    # for part 2
    crates[to_crate].extend(crates[from_crate][-blocks:])
    crates[from_crate] = crates[from_crate][:-blocks]

for crate in crates[1:]:
    print(crate[-1], end='')
