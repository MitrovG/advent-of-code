import os

from util.input import read_string_list

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_string_list(filepath)

score = 0
score_2 = 0
for rnd in data:
    elf, me = rnd.split(' ')
    elf = elf.strip()
    me = me.strip()
    if me == 'X':
        score += 1
        if elf == 'A':
            score += 3
            score_2 += 3
        elif elf == 'C':
            score += 6
            score_2 += 2
        else:
            score_2 += 1
    if me == 'Y':
        score += 2
        score_2 += 3
        if elf == 'B':
            score += 3
            score_2 += 2
        elif elf == 'A':
            score += 6
            score_2 += 1
        else:
            score_2 += 3
    if me == 'Z':
        score += 3
        score_2 += 6
        if elf == 'C':
            score += 3
            score_2 += 1
        elif elf == 'B':
            score += 6
            score_2 += 3
        else:
            score_2 += 2

print(score)
print(score_2)
