from util.FileHelper import read_file_multiple_lines

data = read_file_multiple_lines('2021', 'day9')
y_len = len(data)
x_len = len(data[0].strip())


# d is data
# i is x
# j is y
def get_adjacent_points(i, j):
    points = list()
    if i == 0:
        points.append((i+1, j))
    elif i == x_len - 1:
        points.append((i-1, j))
    else:
        points.append((i+1, j))
        points.append((i-1, j))
    if j == 0:
        points.append((i, j+1))
    elif j == y_len - 1:
        points.append((i, j-1))
    else:
        points.append((i, j+1))
        points.append((i, j-1))
    return points


# Given a starting point, it determines all points that are part of its basin.
# Basins extend from the starting point moving in 4 cardinal directions (no diagonals)
# They stop when they hit a 9 going in any direction.
def get_basin(d, start_i, start_j):
    basin_points = set()  # Ending returned set
    visited = dict()  # A dictionary of a point-tuple to boolean value
    to_visit = set()  # Points to still consider
    to_visit.add((start_i, start_j))
    while len(to_visit) > 0:
        cur_vis = to_visit.pop()  # Get next point to find neighbors of
        basin_points.add(cur_vis)  # Add the point to our basin
        visited[cur_vis] = True  # Set that we've visited the point
        cur_neighbors = get_adjacent_points(cur_vis[0], cur_vis[1])  # Get the neighbors of this point
        for n in cur_neighbors:
            # Basins stop a 9 in any direction, only visit points once.
            if d[n[1]][n[0]] != '9' and not visited.get(n, False):
                to_visit.add(n)
    return basin_points


low_points = list()
low_point_coords = list()
for y in range(y_len):
    for x in range(x_len):
        cur = int(data[y][x])
        adjacent = get_adjacent_points(x, y)
        low = True
        for a in adjacent:
            # Low points are less than all of their adjacent points
            if cur >= int(data[a[1]][a[0]]):
                low = False
                break
        if low:
            low_points.append(cur)
            low_point_coords.append((x, y))

count = 0  # Part 1 solution is sum of low-point values.
basin_sizes = list()
for low_point in low_points:
    count += (low_point + 1)
print(count)

# Part 2
for l_p_c in low_point_coords:
    basin_sizes.append(len(get_basin(data, l_p_c[0], l_p_c[1])))

sorted_sizes = sorted(basin_sizes, reverse=True)
print(sorted_sizes[0] * sorted_sizes[1] * sorted_sizes[2])
