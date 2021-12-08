
with open('input.txt', 'r') as fin:
    data = fin.read().split('\n')

solution_1 = 0
for row in data:
    wires, _, numbers = row.partition('|')
    solution_1 += len([element for element in map(len, numbers.split()) if element in (2, 3, 4, 7)])

#####################################################################################################

decoded = []
for row in data:
    wires, _, numbers = row.partition('|')
    n2s = dict()
    s2n = dict()
    fives = []
    sixes = []
    for wire in wires.split():
        wire = ''.join(sorted(wire))
        if len(wire) == 2:
            n2s[1] = wire
            s2n[wire] = 1
        elif len(wire) == 3:
            n2s[7] = wire
            s2n[wire] = 7
        elif len(wire) == 4:
            n2s[4] = wire
            s2n[wire] = 4
        elif len(wire) == 7:
            n2s[8] = wire
            s2n[wire] = 8
        elif len(wire) == 5:
            fives.append(wire)
        else:
            sixes.append(wire)
    for e_six in sixes:
        e_six = ''.join(sorted(e_six))
        if len(set(e_six).intersection(set(n2s[4]))) == 4:
            n2s[9] = e_six
            s2n[e_six] = 9
        elif len(set(e_six).intersection(set(n2s[7]))) == 3:
            n2s[0] = e_six
            s2n[e_six] = 0
        else:
            n2s[6] = e_six
            s2n[e_six] = 6
    for e_five in fives:
        e_five = ''.join(sorted(e_five))
        if len(set(e_five).intersection(set(n2s[1]))) == 2:
            n2s[3] = e_five
            s2n[e_five] = 3
        elif len(set(e_five).intersection(set(n2s[6]))) == 5:
            n2s[5] = e_five
            s2n[e_five] = 5
        else:
            n2s[2] = e_five
            s2n[e_five] = 2

    decoded_number = 0
    for number in numbers.split():
        decoded_number = decoded_number * 10 + s2n[''.join(sorted(number))]

    decoded.append(decoded_number)

solution_2 = sum(decoded)

######################################################################################################
print(solution_1)
print(solution_2)