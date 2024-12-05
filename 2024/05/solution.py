import os

from util.input import read_string_parts

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_string_parts(filepath)
rules, updates = data


def order_numbers(unordered_numbers):

    new_numbers = []
    un_set = set(unordered_numbers)
    my_rulebook = {}
    for unordered_number in unordered_numbers:
        my_rulebook[unordered_number] = rulebook.get(unordered_number).intersection(un_set)

    visited = set()
    while unordered_numbers:
        element = unordered_numbers.pop(0)
        if len(my_rulebook.get(element).difference(visited)) == 0:
            new_numbers.append(element)
            visited.add(element)
        else:
            unordered_numbers.append(element)

    return new_numbers


rulebook = {}
for rule in rules.split('\n'):
    left, right = map(int, rule.split('|'))
    rulebook.setdefault(left, set())
    rulebook.setdefault(right, set()).add(left)

solution_1 = 0
solution_2 = 0
for update in updates.split('\n'):
    numbers = list(map(int, update.split(',')))
    for i, number in enumerate(numbers):
        required = rulebook.get(number)
        after = set(numbers[i + 1:])
        if len(required.intersection(after)):
            new_numbers = order_numbers(numbers[:])
            solution_2 += new_numbers[len(numbers) // 2]
            break
    else:
        solution_1 += numbers[len(numbers) // 2]

print(solution_1)
print(solution_2)
