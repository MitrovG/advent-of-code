import os

from util.input import read_full

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_full(filepath)
stones = [int(stone) for stone in data.split()]

cache = {}

def count(stone_value, blink_times):

    stone_len = len(str(stone_value))
    if blink_times == 0:
        return 1
    elif (stone_value, blink_times) in cache:
        return cache[(stone_value, blink_times)]
    elif stone_value == 0:
        result =  count(1, blink_times-1)
    elif stone_len % 2 == 0:
        result = count(stone_value // pow(10, stone_len // 2), blink_times - 1) + \
               count(stone_value % pow(10, stone_len // 2), blink_times - 1)
    else:
        result = count(stone_value * 2024, blink_times - 1)
    cache[(stone_value, blink_times)] = result
    return result


solution_1 = 0
solution_2 = 0
for stone in stones:
    solution_1 += count(stone, 25)
    solution_2 += count(stone, 75)


print(solution_1)
print(solution_2)
