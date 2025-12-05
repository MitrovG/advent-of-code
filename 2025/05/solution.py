import os

from util.input import read_string_parts

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_string_parts(filepath)

ranges = [(int(start), int(end)) for r in data[0].split()
          for (start, end) in [r.split('-')]]
ingredients = list(map(int, data[1].split()))

ranges = sorted(ranges, key=lambda x: (x[0], x[1]))
final_ranges = [ranges[0]]
for start, end in ranges[1:]:
    f_start, f_end = final_ranges[-1]
    if start <= f_end:
        if end <= f_end:
            continue
        else:
            final_ranges[-1] = (f_start, end)
    else:
        final_ranges.append((start, end))

solution_1 = 0
for ingredient in ingredients:
    for start, end in final_ranges:
        if start <= ingredient <= end:
            solution_1 += 1
            break

solution_2 = sum(end - start + 1 for (start, end) in final_ranges)

print(solution_1)
print(solution_2)