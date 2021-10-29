import collections
from util.FileHelper import read_file_multiple_lines

directions = read_file_multiple_lines("2016", "day8")


def create_rect(matrix, width, height):
    for j in range(height):
        for i in range(width):
            matrix[j][i] = '#'


def rotate_row(matrix, row, shiftBy):
    the_row = collections.deque(matrix[row])
    the_row.rotate(shiftBy)
    matrix[row] = list(the_row)


def rotate_column(matrix, col, shiftBy):
    newCol = list()
    for r in range(len(matrix)):
        newCol.append(matrix[r-shiftBy][col])

    for r in range(len(newCol)):
        matrix[r][col] = newCol[r]

def count_pixels(matrix):
    count = 0
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == '#':
                count += 1

    return count

m = [['.' for w in range(50)] for h in range(6)]

for direction in directions:
    if "rect" in direction:
        dimensions = direction.strip().split(' ')[1].split('x')
        create_rect(m, int(dimensions[0]), int(dimensions[1]))
    else:
        parts = direction.strip().split(' ')
        shiftBy = int(parts[4])
        rowCol = int(parts[2].strip().split('=')[1])
        if "column" in direction:
            rotate_column(m, rowCol, shiftBy)
        elif "row" in direction:
            rotate_row(m, rowCol, shiftBy)

print(count_pixels(m))

# Part Two
for r in range(len(m)):
    print(m[r])
