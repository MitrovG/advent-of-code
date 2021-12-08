
with open('input.txt', 'r') as fin:
    numbers = list(map(int, fin.readline().split(',')))
    fin.readline()
    data = fin.read().split('\n\n')

boards = []
for row in data:
    board = []
    board_rows = row.split('\n')
    for board_row in board_rows:
        for value in board_row.split():
            board.append(int(value))
    boards.append(board)


def is_winner(board):
    for idx in range(5):
        if not any(board[idx*5 + key] for key in range(5)):
            return True
        if not any(board[key*5 + idx] for key in range(5)):
            return True
    return False


def find_element(board, element):
    for idx, value in enumerate(board):
        if value == element:
            board[idx] = None
            break


winning_boards = []
for number in numbers:
    for idx, board in enumerate(boards):
        if idx in [i for i, _ in winning_boards]:
            continue
        find_element(board, number)
        if is_winner(board):
            winning_boards.append((idx, number))

solution_1 = sum(filter(None, boards[winning_boards[0][0]])) * winning_boards[0][1]
solution_2 = sum(filter(None, boards[winning_boards[-1][0]])) * winning_boards[-1][1]
print(solution_1)
print(solution_2)