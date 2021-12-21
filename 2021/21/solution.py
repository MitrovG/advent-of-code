from itertools import product

with open('input.txt', 'r') as fin:
    data = fin.read().split('\n')

position_1 = int(data[0].split(':')[1])
position_2 = int(data[1].split(':')[1])

# Part 1
points_1, points_2 = 0, 0
dice = 0


def move_position(position: int, dice: int):
    movement = (3 * dice + 6) % 10

    return (position + movement - 1) % 10 + 1


while True:
    position_1 = move_position(position_1, dice)
    points_1 += position_1
    dice += 3
    if points_1 >= 1000:
        solution_1 = points_2 * dice
        break
    position_2 = move_position(position_2, dice)
    points_2 += position_2
    dice += 3
    if points_2 >= 1000:
        solution_1 = points_1 * dice
        break

print(solution_1)

# Part 2

position_1 = int(data[0].split(':')[1])
position_2 = int(data[1].split(':')[1])

roll_combos = list(product([1, 2, 3], repeat=3))
cache = dict()


def count_wins(position_1, position_2, points_1, points_2):

    if points_1 >= 21:
        return 1, 0
    if points_2 >= 21:
        return 0, 1

    key = (position_1, position_2, points_1, points_2)
    if key in cache:
        return cache[key]

    player_1_wins = 0
    player_2_wins = 0
    for roll_combo in roll_combos:
        new_position_1 = ((position_1 + sum(roll_combo) - 1) % 10) + 1
        new_points_1 = points_1 + new_position_1
        new_player_2_wins, new_player_1_wins = count_wins(position_2, new_position_1, points_2, new_points_1)
        player_1_wins += new_player_1_wins
        player_2_wins += new_player_2_wins

    cache[key] = (player_1_wins, player_2_wins)

    return player_1_wins, player_2_wins


solution_2 = max(count_wins(position_1, position_2, 0, 0))
print(solution_2)
