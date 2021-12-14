from collections import Counter

with open('input.txt', 'r') as fin:
    data = fin.read().split('\n\n')

polymer_template = data[0]
rules = {key: value for key, _, value in (rule.partition(' -> ') for rule in data[1].split('\n'))}

pairs = Counter([(x, y) for x, y in zip(polymer_template[:-1], polymer_template[1:])])


def solve(pairs):
    letters = Counter()
    letters[polymer_template[-1]] += 1
    for (letter, _), count in pairs.items():
        letters[letter] += count

    most_common = letters.most_common()
    highest = most_common[0][1]
    lowest = most_common[-1][1]

    return highest - lowest


for step in range(40):
    new_pairs = Counter()
    for pair, pair_cnt in pairs.items():
        first_letter, second_letter = pair
        new_letter = rules.get(''.join(pair))
        new_pairs[(first_letter, new_letter)] += pair_cnt
        new_pairs[(new_letter, second_letter)] += pair_cnt
    pairs = new_pairs
    if step + 1 == 10:
        solution_1 = solve(pairs)

solution_2 = solve(pairs)
print(solution_1)
print(solution_2)
