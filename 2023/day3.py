from util.FileHelper import read_file_multiple_lines
from util.MatrixUtils import get_2d_neighbor_points_bounded

lines = read_file_multiple_lines('2023', 'day3')

# Part numbers take up multiple cells of the grid, so each one needs to refer to the full sum.
point_to_partNumber = dict()
potential_gears = list()

# bounds for getting neighbors later
y_max = len(lines) - 1
x_max = len(lines[0].strip()) - 1


def add_part_points(part_points, part_number):
    for part_point in part_points:
        point_to_partNumber[part_point] = part_number


# Looks at all neighbors around the point.  If any of them are a symbol, returns true, otherwise false.
def is_point_part(point_to_check):
    neighbors = get_2d_neighbor_points_bounded(point_to_check[0], point_to_check[1], 0, 0, x_max, y_max)
    for neighbor in neighbors:
        value = lines[neighbor[1]][neighbor[0]]

        if value.isnumeric() or value == '.':
            continue

        return True
    return False


part_sum = 0
cur_part_number = ""
cur_part_points = list()
cur_is_part = False
for y in range(len(lines)):
    for x in range(len(lines[y])):
        cur = lines[y][x]
        cur_point = (x, y)
        if cur == '*':
            potential_gears.append(cur_point)

        if cur.isnumeric():
            cur_part_number += cur
            cur_part_points.append(cur_point)
            if is_point_part(cur_point):
                cur_is_part = True
        else:
            # Returns True is string isn't empty (hence a number was built)
            if cur_part_number:
                if cur_is_part:
                    part_sum += int(cur_part_number)
                add_part_points(cur_part_points, int(cur_part_number))
                cur_part_number = ""
                cur_part_points.clear()
                cur_is_part = False

print(part_sum)

# Part 2, loop through gears, see if it's neighbors are included in point_to_partNumber keys.
# Sum up products that have exactly 2 adjacent parts.
gear_ratio_sum = 0
for potential_gear in potential_gears:
    neighbors = get_2d_neighbor_points_bounded(potential_gear[0], potential_gear[1], 0, 0, x_max, y_max)
    neighboring_parts = set()
    for neighbor in neighbors:
        if neighbor in point_to_partNumber:
            neighboring_parts.add(point_to_partNumber[neighbor])
    if len(neighboring_parts) == 2:
        gear_ratio = 1
        for gear_part in neighboring_parts:
            gear_ratio *= gear_part
        gear_ratio_sum += gear_ratio

print(gear_ratio_sum)