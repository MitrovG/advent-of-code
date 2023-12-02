import os

from util.input import read_string_list

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_string_list(filepath)

MAXIMUM = {
    'red': 12,
    'green': 13,
    'blue': 14
}

solution_1 = 0
solution_2 = 0
for idx, row in enumerate(data):
    solution_1 += (idx + 1)
    flag = False
    value = row.split(':')[1]
    reveals = value.split(';')
    max_per_game = {'green': 0, 'red': 0, 'blue': 0}
    for reveal in reveals:
        colors = reveal.split(',')
        for color_info in colors:
            number, color = color_info.strip().split(' ')
            if int(number) > MAXIMUM[color]:
                flag = True
            max_per_game[color] = max(int(number), max_per_game[color])

    if flag:
        solution_1 -= (idx + 1)
    solution_2 += (max_per_game['green'] * max_per_game['red'] * max_per_game['blue'])

print(solution_1)
print(solution_2)