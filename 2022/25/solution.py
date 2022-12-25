from __future__ import annotations
import os

from util.input import read_string_list

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_string_list(filepath)


def snafu_to_decimal(snafu_num: str) -> int:

    decimal = 0
    for idx, snafu_digit in enumerate(snafu_num[::-1]):
        try:
            snafu_digit = int(snafu_digit)
        except ValueError:
            if snafu_digit == '=':
                snafu_digit = -2
            elif snafu_digit == '-':
                snafu_digit = -1

        decimal += snafu_digit * pow(5, idx)

    return decimal


def decimal_to_snafu(decimal_num: int) -> str:

    snafu = ''
    while decimal_num > 0:
        digit = decimal_num % 5
        if digit < 3:
            snafu += str(digit)
            remainder = 0
        else:
            if digit == 3:
                snafu += '='
            else:
                snafu += '-'
            remainder = 1

        decimal_num //= 5
        decimal_num += remainder

    return snafu[::-1]


result = 0
for snafu_number in data:
    result += snafu_to_decimal(snafu_number)

solution_1 = decimal_to_snafu(result)
print(solution_1)
