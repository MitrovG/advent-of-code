import os

from util.input import read_matrix_num

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_matrix_num(filepath)
solution_1 = 0
solution_2 = 0


def check_possible(diff):
    return all(True if 1 <= e_diff <= 3 else False for e_diff in diff) or \
            all(True if -1 >= e_diff >= -3 else False for e_diff in diff)


for row in data:
    row_diff = [x - y for x, y in zip(row[1:], row[:-1])]
    if check_possible(row_diff):
        solution_1 += 1
        solution_2 += 1
    elif check_possible(row_diff[1:]) or check_possible(row_diff[:-1]):
        solution_2 += 1
    else:
        for i in range(len(row_diff) - 1):
            new_row_diff = row_diff[:]
            new_row_diff[i] = new_row_diff[i] + new_row_diff[i + 1]
            new_row_diff.pop(i+1)
            if check_possible(new_row_diff):
                solution_2 += 1
                break

print(solution_1)
print(solution_2)
