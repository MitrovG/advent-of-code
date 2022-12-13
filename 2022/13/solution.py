import os

from util.input import read_string_parts

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_string_parts(filepath)


def first_smaller(left, right):

    if len(left) == len(right) == 0:
        return None
    if len(left) == 0:
        return True
    if len(right) == 0:
        return False

    x = left[0]
    y = right[0]
    if isinstance(x, list) and not isinstance(y, list):
        return first_smaller(left, [[y]] + right[1:])
    elif not isinstance(x, list) and isinstance(y, list):
        return first_smaller([[x]] + left[1:], right)
    elif isinstance(x, list) and isinstance(y, list):
        result = first_smaller(x, y)
        return result if result is not None else first_smaller(left[1:], right[1:])
    else:
        if x < y:
            return True
        elif x > y:
            return False
        else:
            return first_smaller(left[1:], right[1:])


packet_a = [[2]]
packet_b = [[6]]
smaller_a = 1
smaller_b = 2

idx = 0
solution_1 = 0
for pair in data:
    idx += 1
    first, second = map(eval, pair.split('\n'))
    if first_smaller(first, second):
        solution_1 += idx
    if first_smaller(first, packet_a):
        smaller_a += 1
    if first_smaller(second, packet_a):
        smaller_a += 1
    if first_smaller(first, packet_b):
        smaller_b += 1
    if first_smaller(second, packet_b):
        smaller_b += 1

print(solution_1)
solution_2 = smaller_b * smaller_a
print(solution_2)
