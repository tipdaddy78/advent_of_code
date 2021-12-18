import sys

from util.FileHelper import read_file_multiple_lines
from collections import deque

data = read_file_multiple_lines('2021', 'day15')
points = dict()
for y in range(len(data)):
    for x in range(len(data[y].strip())):
        points[(x, y)] = int(data[y][x])

lengths = (len(data[0].strip()), len(data))
end = (len(data[0].strip()) - 1, len(data) - 1)


def get_neighbors(p, cur_x, cur_y):
    neighbors = list()
    if (cur_x + 1, cur_y) in p:
        neighbors.append((cur_x + 1, cur_y))
    if (cur_x - 1, cur_y) in p:
        neighbors.append((cur_x - 1, cur_y))
    if (cur_x, cur_y + 1) in p:
        neighbors.append((cur_x, cur_y + 1))
    if (cur_x, cur_y - 1) in p:
        neighbors.append((cur_x, cur_y - 1))
    return neighbors


def path_find(points_to_search):
    distances = dict()
    visited = set()
    to_visit = deque()
    to_visit.append((0, 0))
    while len(to_visit) > 0:
        cur = to_visit.popleft()
        for n in get_neighbors(points_to_search, cur[0], cur[1]):
            if n not in visited or distances[cur] + points_to_search[n] < distances.get(n, sys.maxsize):
                if n not in to_visit:
                    to_visit.append(n)
                d = distances.get(cur, 0) + points_to_search[n]
                if d < distances.get(n, sys.maxsize):
                    distances[n] = d
        visited.add(cur)
    return distances


print(path_find(points)[end])

# Part 2 - Generating larger input, then search again
points_2 = points.copy()
max_x = 0
max_y = 0
for dx in range(5):
    for dy in range(5):
        # dx and dy of 0 is the original points, don't need to recreate them.
        if dx == 0 and dy == 0:
            continue
        for k in points.keys():
            x = (dx * lengths[0]) + k[0]
            y = (dy * lengths[1]) + k[1]
            max_x = max(x, max_x)
            max_y = max(y, max_y)
            v = points[k]
            for i in range(dx + dy):
                v = (v + 1) % 10
                if v == 0:
                    v = 1
            points_2[(x, y)] = v

print(max_x, max_y)
print(path_find(points_2)[(max_x, max_y)])
