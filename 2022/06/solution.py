import os

from util.input import read_full

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_full(filepath)

solution_1 = 0
solution_2 = 0

for idx in range(len(data)):
    if solution_1 == 0 and len(set(data[idx: idx + 4])) == 4:
        solution_1 = idx + 4
    if solution_2 == 0 and len(set(data[idx: idx + 14])) == 14:
        solution_2 = idx + 14

print(solution_1)
print(solution_2)
