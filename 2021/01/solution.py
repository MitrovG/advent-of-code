

with open('input.txt', 'r') as fin:
    numbers = [int(num) for num in fin.read().split('\n')]

solution_1 = sum([1 if y > x else 0 for (x, y) in zip(numbers[:-1], numbers[1:])])

solution_2 = sum([1 if y > x else 0 for (x, y) in zip(numbers[:-3], numbers[3:])])

print(solution_1)
print(solution_2)