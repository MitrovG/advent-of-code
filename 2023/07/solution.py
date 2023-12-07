import os
import re
from collections import Counter

from util.input import read_string_list

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_string_list(filepath)


def first_rank(hand: str, part_2: bool = False):

    j_counter = 0
    if part_2 and 'J' in hand:
        hand = re.sub('J', '', hand)
        j_counter = 5 - len(hand)
    cntr = Counter(hand)
    vals = list(sorted(cntr.values()))
    if part_2:
        if vals:
            vals[-1] += j_counter
        else:
            return 7
    if len(vals) == 1:
        return 7
    if len(vals) == 2:
        if vals[0] == 4 or vals[1] == 4:
            return 6
        else:
            return 5
    if len(vals) == 3:
        if vals[0] == 3 or vals[1] == 3 or vals[2] == 3:
            return 4
        else:
            return 3
    if len(vals) == 4:
        return 2
    return 1


def second_rank(hand: str, part_2: bool = False):

    key = 'AKQJT'
    if part_2:
        value = 'ZYX1V'
    else:
        value = 'ZYXWV'
    return hand.translate(str.maketrans(key, value))


hands = [(row.split()[0], int(row.split()[1])) for row in data]
hands.sort(key=lambda x: (first_rank(x[0]), second_rank(x[0])))

solution_1 = 0
for idx, (hand, bid) in enumerate(hands):
    solution_1 += (idx + 1) * bid

print(solution_1)

hands.sort(key=lambda x: (first_rank(x[0], True), second_rank(x[0], True)))

solution_2 = 0
for idx, (hand, bid) in enumerate(hands):
    solution_2 += (idx + 1) * bid

print(solution_2)
