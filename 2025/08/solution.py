import math
import os

from util.input import read_string_list

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_string_list(filepath)


def compute_distance(box1, box2):

    return math.sqrt(sum((b1 - b2) ** 2 for b1, b2 in zip(box1, box2)))


# Create junction boxes
junction_boxes = []
for row in data:
    x, y, z = map(int, row.split(','))
    junction_boxes.append((x, y, z))

# Compute distances
distances = []
for idx_1, box1 in enumerate(junction_boxes[:-1]):
    for idx_2, box2 in enumerate(junction_boxes[idx_1 + 1:]):
        distance = compute_distance(box1, box2)
        distances.append((idx_1, idx_2 + idx_1 + 1, distance))
distances = sorted(distances, key=lambda x: -x[2])
# Define circuits
circuits = {}
for idx in range(len(junction_boxes)):
    circuits[idx] = {idx}

# Connections
counter = 0
while True:
    counter += 1
    jb1, jb2, _ = distances.pop()
    c1 = circuits[jb1]
    c2 = circuits[jb2]
    if c1 == c2:
        continue
    c3 = c1.union(c2)
    for jb in c3:
        circuits[jb] = c3

    # Part 1 solution
    if counter == 1000:
        circuits_length = []
        visited = set()
        for jb, circuit in circuits.items():
            if jb not in visited:
                circuits_length.append(len(circuit))
                for jb_circuit in circuit:
                    visited.add(jb_circuit)
        solution_1 = math.prod(sorted(circuits_length, reverse=True)[:3])

    # Part 2 solution
    if len(c3) == len(junction_boxes):
        solution_2 = junction_boxes[jb1][0] * junction_boxes[jb2][0]
        break

print(solution_1)
print(solution_2)