from typing import List


def read_integer_list(filepath: str) -> List[int]:
    with open(filepath, 'r') as fin:
        integers = [int(num) for num in fin.read().split('\n')]

    return integers


def read_string_list(filepath: str) -> List[str]:
    with open(filepath, 'r') as fin:
        data = fin.read().split('\n')

    return data


def read_full(filepath: str) -> str:
    with open(filepath, 'r') as fin:
        data = fin.read()

    return data


def read_matrix(filepath: str) -> List[List[int]]:
    with open(filepath, 'r') as fin:
        data = [[int(number) for number in row] for row in fin.read().split('\n')]

    return data


def read_string_parts(filepath: str) -> List[str]:
    with open(filepath, 'r') as fin:
        data = fin.read().split('\n\n')

    return data


def read_matrix_str(filepath: str) -> List[List[str]]:
    with open(filepath, 'r') as fin:
        data = [[char for char in row] for row in fin.read().split('\n')]

    return data
