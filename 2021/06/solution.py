
with open('input.txt', 'r') as fin:
    data = fin.read().split(',')

fishes = [0] * 9
for fish_timer in map(int, data):
    fishes[fish_timer] += 1


def simulate_days(days: int, fishes):
    for i in range(days):
        fishes = fishes[1:] + [fishes[0]]
        fishes[6] += fishes[-1]

    return sum(fishes)


solution_1 = simulate_days(80, fishes)
solution_2 = simulate_days(256, fishes)

print(solution_1)
print(solution_2)