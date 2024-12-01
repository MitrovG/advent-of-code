import os
from collections import Counter

from util.input import read_matrix_num

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_matrix_num(filepath)

first_l = sorted([x for x, _ in data])
second_l = sorted([y for _, y in data])
second_l_counter = Counter(second_l)

solution_1 = sum(abs(x - y) for x, y in zip(first_l, second_l))
solution_2 = sum(x * second_l_counter[x] for x in first_l)

print(solution_1)
print(solution_2)
