
with open('input.txt', 'r') as fin:
    data = fin.read()

rows = data.split('\n')
height = len(rows)
width = len(rows[0])

east = set()
south = set()
for r_idx, row in enumerate(rows):
    for c_idx, value in enumerate(row):
        if value == '>':
            east.add((r_idx, c_idx))
        elif value == 'v':
            south.add((r_idx, c_idx))

steps = 0
while True:
    steps += 1
    movement = False

    new_east = set()
    for r, c in sorted(east):
        cc = (c + 1) % width
        if (r, cc) not in east and (r, cc) not in south:
            new_east.add((r, cc))
            movement = True
        else:
            new_east.add((r, c))
    east = new_east

    new_south = set()
    for r, c in sorted(south):
        rr = (r + 1) % height
        if (rr, c) not in east and (rr, c) not in south:
            new_south.add((rr, c))
            movement = True
        else:
            new_south.add((r, c))
    south = new_south

    if not movement:
        print(steps)
        break
