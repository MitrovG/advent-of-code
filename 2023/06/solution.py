import os
import re

from util.input import read_string_list

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_string_list(filepath)

time = [int(x) for x in re.findall(r'\d+', data[0])]
distance = [int(x) for x in re.findall(r'\d+', data[1])]

solution_1 = 1
for t, d in zip(time, distance):

    for i in range(t):
        if i * (t - i) > d:
            solution_1 *= (t - i - i + 1)
            break
print(solution_1)

solution_2 = 0
new_time = int(''.join([str(t) for t in time]))
new_distance = int(''.join([str(d) for d in distance]))

for ii in range(new_time):
    if ii * (new_time - ii) > new_distance:
        solution_2 = new_time - ii - ii + 1
        break

print(solution_2)
