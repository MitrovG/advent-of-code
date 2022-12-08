import os

from util.input import read_matrix

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_matrix(filepath)

solution_1 = len(data) * 2 + (len(data) - 2) * 2
visible = set()
scenic_view = dict()

r = 1
while r < len(data) - 1:

    l_max = data[r][0]
    l_max_i = 0
    c = 1
    while c < len(data[r]) - 1:
        if data[r][c] > l_max:
            visible.add((r, c))
            l_max = data[r][c]
            l_max_i = c
            scenic_view[(r, c)] = scenic_view.get((r, c), 1) * c
        elif data[r][c] == l_max:
            scenic_view[(r, c)] = scenic_view.get((r, c), 1) * (c - l_max_i)
            l_max_i = c
        else:
            for i in range(c - l_max_i):
                if data[r][c] < data[r][c-i+1]:
                    scenic_view[(r, c)] = scenic_view.get((r, c), 1) * (i + 1)
                    break
        c += 1

    r_max = data[r][-1]
    r_max_i = len(data[r]) - 1
    c = len(data[r]) - 2
    while c > 0:
        if data[r][c] > r_max:
            visible.add((r, c))
            r_max = data[r][c]
            r_max_i = c
            scenic_view[(r, c)] = scenic_view.get((r, c), 1) * (len(data[r]) - 1 - c)
        elif data[r][c] == r_max:
            scenic_view[(r, c)] = scenic_view.get((r, c), 1) * (r_max_i - c)
            r_max_i = c
        else:
            for i in range(r_max_i - c):
                if data[r][c] <= data[r][c+i+1]:
                    scenic_view[(r, c)] = scenic_view.get((r, c), 1) * (i + 1)
                    break
        c -= 1

    r += 1

c = 1
while c < len(data[0]) - 1:

    u_max = data[0][c]
    u_max_i = 0
    r = 1
    while r < len(data) - 1:
        if data[r][c] > u_max:
            visible.add((r, c))
            u_max = data[r][c]
            u_max_i = r
            scenic_view[(r, c)] = scenic_view.get((r, c), 1) * r
        elif data[r][c] == u_max:
            scenic_view[(r, c)] = scenic_view.get((r, c), 1) * (r - u_max_i)
            u_max_i = r
        else:
            for i in range(r - u_max_i):
                if data[r][c] < data[r-1+1][c]:
                    scenic_view[(r, c)] = scenic_view.get((r, c), 1) * (i + 1)
                    break
        r += 1

    d_max = data[-1][c]
    d_max_i = len(data) - 1
    r = len(data) - 2
    while r > 0:
        if data[r][c] > d_max:
            visible.add((r, c))
            d_max = data[r][c]
            d_max_i = r
            scenic_view[(r, c)] = scenic_view.get((r, c), 1) * (len(data) - 1 - r)
        elif data[r][c] >= d_max:
            scenic_view[(r, c)] = scenic_view.get((r, c), 1) * (d_max_i - r)
            d_max_i = r
        else:
            for i in range(d_max_i - r):
                if data[r][c] <= data[r+i+1][c]:
                    scenic_view[(r, c)] = scenic_view.get((r, c), 1) * (i + 1)
                    break
        r -= 1

    c += 1

solution_1 += len(visible)
print(solution_1)
print(scenic_view[max(scenic_view, key=scenic_view.get)])