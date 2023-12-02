import os

from util.input import read_string_list

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_string_list(filepath)

WORD_DIGITS = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

solution_1 = 0
solution_2 = 0
for row in data:
    only_digits = []
    digits_and_words = []
    for idx, letter in enumerate(row):
        if letter.isdigit():
            only_digits.append(int(letter))
            digits_and_words.append(int(letter))
        for word, digit in WORD_DIGITS.items():
            if row[idx:].startswith(word):
                digits_and_words.append(digit)
    number = 10 * only_digits[0] + only_digits[-1]
    solution_1 += number
    number_2 = 10 * digits_and_words[0] + digits_and_words[-1]
    solution_2 += number_2

print(solution_1)
print(solution_2)
