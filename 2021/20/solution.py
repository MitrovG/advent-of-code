
with open('input.txt', 'r') as fin:
    data = fin.read().split('\n\n')

algorithm = [1 if element == '#' else 0 for element in data[0]]
image = [[1 if element == '#' else 0 for element in row] for row in data[1].split('\n')]

infinite_image = 0

solution_1 = None
solution_2 = None
for step in range(1, 51):
    new_image = []
    for x in range(-1, len(image) + 1):
        new_image_row = []
        for y in range(-1, len(image[0]) + 1):

            binary_number = ''
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= x + i < len(image) and 0 <= y + j < len(image[0]):
                        binary_digit = image[x + i][y + j]
                    else:
                        binary_digit = infinite_image
                    binary_number += str(binary_digit)
            decimal_number = int(binary_number, 2)
            pixel = algorithm[decimal_number]
            new_image_row.append(pixel)
        new_image.append(new_image_row)

    image = new_image[:]
    infinite_image = algorithm[0] if infinite_image == 0 else algorithm[-1]

    if step == 2:
        solution_1 = sum(sum(e) for e in image)
    if step == 50:
        solution_2 = sum(sum(e) for e in image)

print(solution_1)
print(solution_2)
