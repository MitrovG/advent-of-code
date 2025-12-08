import os
import math
from itertools import zip_longest

from util.input import read_string_list

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_string_list(filepath)
numbers = [[int(element) for element in row.split()] for row in data[:-1]]
operators = data[-1].split()

numbers_2 = []
numbers_2_sublist = []
for chars in zip_longest(*data[:-1], fillvalue=' '):
    try:
        new_element = int(''.join(chars))
        numbers_2_sublist.append(new_element)
    except ValueError:
        numbers_2.append(numbers_2_sublist)
        numbers_2_sublist = []
numbers_2.append(numbers_2_sublist)

solution_1 = 0
solution_2 = 0
for idx in range(len(numbers[0])):
    elements_1 = [numbers[i][idx] for i in range(len(numbers))]
    elements_2 = numbers_2[idx]
    if operators[idx] == '+':
        solution_1 += sum(elements_1)
        solution_2 += sum(elements_2)
    elif operators[idx] == '*':
        solution_1 += math.prod(elements_1)
        solution_2 += math.prod(elements_2)

print(solution_1)
print(solution_2)
