import os

from util.input import read_matrix_str

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

grid = read_matrix_str(filepath)

directions = {
    'R': (0, 1),
    'L': (0, -1),
    'U': (-1, 0),
    'D': (1, 0)
}
LEN_ROW = len(grid)
LEN_COL = len(grid[0])

solution_2 = 0
initial_beams = []
for i in range(LEN_ROW):
    initial_beams.append((i, -1, 'R'))
    initial_beams.append((i, LEN_COL, 'L'))
for i in range(LEN_COL):
    initial_beams.append((-1, i, 'D'))
    initial_beams.append((LEN_ROW, i, 'U'))
for initial_beam in initial_beams:
    beams = [initial_beam]
    energized = set()
    seen = set()
    while beams:
        new_beams = []
        for beam_x, beam_y, beam_direction in beams:
            if 0 <= beam_x < LEN_ROW and 0 <= beam_y < LEN_COL:
                energized.add((beam_x, beam_y))
            if (beam_x, beam_y, beam_direction) in seen:
                continue
            else:
                seen.add((beam_x, beam_y, beam_direction))
            direction_values = directions[beam_direction]
            x, y = beam_x + direction_values[0], beam_y + direction_values[-1]
            if x < 0 or x >= LEN_ROW or y < 0 or y >= LEN_COL:
                continue
            else:
                space_value = grid[x][y]
            if space_value == '.' or \
                    (space_value == '-' and beam_direction in ('L', 'R')) or \
                    (space_value == '|' and beam_direction in ('U', 'D')):
                new_beams.append((x, y, beam_direction))
            elif space_value == '-' and beam_direction in ('U', 'D'):
                new_beams.append((x, y, 'L'))
                new_beams.append((x, y, 'R'))
            elif space_value == '|' and beam_direction in ('L', 'R'):
                new_beams.append((x, y, 'U'))
                new_beams.append((x, y, 'D'))
            elif space_value == '/':
                if beam_direction == 'U':
                    new_direction = 'R'
                elif beam_direction == 'R':
                    new_direction = 'U'
                elif beam_direction == 'D':
                    new_direction = 'L'
                else:
                    new_direction = 'D'
                new_beams.append((x, y, new_direction))
            elif space_value == '\\':
                if beam_direction == 'U':
                    new_direction = 'L'
                elif beam_direction == 'L':
                    new_direction = 'U'
                elif beam_direction == 'D':
                    new_direction = 'R'
                else:
                    new_direction = 'D'
                new_beams.append((x, y, new_direction))
            else:
                continue
        beams = new_beams
    if initial_beam == (0, -1, 'R'):
        solution_1 = len(energized)
        print(solution_1)
    if len(energized) > solution_2:
        solution_2 = len(energized)

print(solution_2)
