
with open('input.txt', 'r') as fin:
    data = fin.read().split('\n')

brackets = {
    '{': '}',
    '(': ')',
    '[': ']',
    '<': '>'
}

part_1_points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

part_2_points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

solution_1 = 0
solution_2_sums = []
for line in data:
    line_stack = []
    corrupt = False
    for char in line:
        if char in brackets:
            line_stack.append(char)
        elif brackets[line_stack[-1]] == char:
            line_stack.pop()
        else:
            solution_1 += part_1_points[char]
            corrupt = True
            break
    if not corrupt:
        sum_invalid = 0
        for char in reversed(line_stack):
            value = part_2_points[brackets[char]]
            sum_invalid = sum_invalid * 5 + value
        solution_2_sums.append(sum_invalid)

solution_2 = sorted(solution_2_sums)[len(solution_2_sums) // 2]

print(solution_1)
print(solution_2)