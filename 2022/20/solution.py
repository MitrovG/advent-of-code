from __future__ import annotations
import os

from util.input import read_integer_list

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_integer_list(filepath)

part_1 = True


class Node:

    def __init__(self, val: int, previous_: Node = None, next_: Node = None):
        self.value = val
        self.previous = previous_
        self.next = next_


# Set up nodes
DECRYPTION_KEY = 811589153 if not part_1 else 1
zero_node = None
first_node = Node(data[0] * DECRYPTION_KEY)
previous_node = first_node
for value in data[1:]:
    current_node = Node(value * DECRYPTION_KEY, previous_=previous_node)
    if value == 0:
        zero_node = current_node
    previous_node.next = current_node
    previous_node = current_node
previous_node.next = first_node
first_node.previous = previous_node

queue = [first_node]
current = first_node.next
while current != first_node:
    queue.append(current)
    current = current.next

for idx in range(10):
    print(f'Starting {idx + 1} shuffling.')
    for node in queue:
        number = node.value
        if number > 0:
            number = number % (len(queue) - 1)
            while number > 0:
                node.next.next.previous = node
                node.next.previous = node.previous
                node.previous.next = node.next
                node.previous = node.next
                node.next = node.next.next
                node.previous.next = node
                number -= 1
        if number < 0:
            number = abs(number) % (len(queue) - 1)
            while number > 0:
                node.previous.previous.next = node
                node.previous.next = node.next
                node.next.previous = node.previous
                node.next = node.previous
                node.previous = node.previous.previous
                node.next.previous = node
                number -= 1

    if idx in (0, 9):
        current = zero_node
        solution_1 = 0
        solution_2 = 0
        for i in range(3001):
            if i in (1000, 2000, 3000):
                solution_1 += current.value
                solution_2 += current.value
            current = current.next
        if idx == 0 and part_1:
            print(f'Solution 1: {solution_1}')
            break
        else:
            print(f'Solution 2: {solution_2}')

# TODO: This solution takes some time to execute (10-15 seconds for part 1 and 1-2 minutes for part 2)
# TODO: This can be further optimized by not moving all items but just the end ones for one node
