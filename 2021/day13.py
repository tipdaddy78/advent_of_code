from util.FileHelper import read_file_multiple_lines


def fold_x(matrix, x_to_fold):
    left_side = list()
    right_side = list()
    for row in matrix:
        left_side.append(row[:x_to_fold])
        to_append = row[x_to_fold + 1:]
        to_append.reverse()
        right_side.append(to_append)

    diff = len(left_side[0]) - len(right_side[0])
    if diff > 0:
        for row in range(len(right_side)):
            for i in range(abs(diff)):
                right_side[row].insert(0, '.')
    elif diff < 0:
        for row in range(len(left_side)):
            for i in range(abs(diff)):
                left_side[row].append('.')

    new_matrix = list()
    for y in range(len(left_side)):
        new_list = list()
        for x in range(len(left_side[0])):
            if left_side[y][x] == '#' or right_side[y][x] == '#':
                new_list.append('#')
            else:
                new_list.append('.')
        new_matrix.append(new_list)
    return new_matrix


def fold_y(matrix, y_to_fold):
    top_side = matrix[:y_to_fold]
    bottom_side = matrix[y_to_fold + 1:]
    diff = len(bottom_side) - len(top_side)
    # If the sides are mismatched, add empty cells to appropriate side.
    if diff < 0:
        for i in range(abs(diff)):
            bottom_side.append(['.' for j in range(len(bottom_side[0]))])
    elif diff > 0:
        for i in range(abs(diff)):
            top_side.insert(0, ['.' for j in range(len(top_side[0]))])

    new_matrix = list()
    for y in range(len(top_side)):
        new_list = list()
        for x in range(len(top_side[0])):
            if top_side[y][x] == '#' or bottom_side[((y + 1) * -1)][x] == '#':
                new_list.append('#')
            else:
                new_list.append('.')
        new_matrix.append(new_list)
    return new_matrix


def get_visible_count(matrix):
    count = 0
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == '#':
                count += 1
    return count


m = None
max_x = 0
max_y = 0
data = read_file_multiple_lines('2021', 'day13')
points = list()
folding = False
folds = 0
for line in data:
    if line.strip() == '':
        folding = True
        # Reached the end of the points time to create the matrix.
        m = [['.' for x in range(max_x+1)] for y in range(max_y+1)]
        for p in points:
            m[p[1]][p[0]] = '#'
    elif folding:
        direction = line.strip().split(' ')[2].split('=')
        if direction[0] == 'x':
            m = fold_x(m, int(direction[1]))
        else:
            m = fold_y(m, int(direction[1]))
        folds += 1
        visible = get_visible_count(m)
        print("After", folds, "folds, there are", visible, "points visible.")
    else:
        coords = line.strip().split(',')
        max_x = max(int(coords[0]), max_x)
        max_y = max(int(coords[1]), max_y)
        points.append((int(coords[0]), int(coords[1])))

# Print final result
for y in range(len(m)):
    line = ''
    for x in range(len(m[0])):
        line += m[y][x]
    print(line)
