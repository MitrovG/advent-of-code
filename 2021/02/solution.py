
with open('input.txt', 'r') as fin:
    data = fin.read().split('\n')

horizontal = depth1 = 0
depth2 = aim = 0

for line in data:
    command, value = line.split()
    value = int(value)
    if command == 'forward':
        horizontal += value
        depth2 += aim * value
    elif command == 'up':
        depth1 -= value
        aim -= value
    elif command == 'down':
        depth1 += value
        aim += value

solution_1 = horizontal * depth1
solution_2 = horizontal * depth2

print(solution_1)
print(solution_2)