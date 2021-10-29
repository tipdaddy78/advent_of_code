from util.PathFinding import bfs_matrix_goal
from copy import deepcopy

# puz_input = 10 # Test input
puz_input = 1364 # Actual input


def is_wall(x, y):
    start = x * x + 3 * x + 2 * x * y + y + y * y
    start += puz_input
    b_form = bin(start)
    # if odd 1's it's a wall, otherwise open
    return b_form.count('1') % 2 != 0


maze = [['#' if is_wall(x, y) else '.' for x in range(200)] for y in range(200)]
vis_orig = [[False for x in range(200)] for y in range(200)]
vis = deepcopy(vis_orig)

path = bfs_matrix_goal(maze, vis, 1, 1, 31, 39)
print(path)
print(len(path) - 1)

# Part 2
locations = set()
for x in range(200):
    for y in range(200):
        if maze[y][x] == '.':
            vis = deepcopy(vis_orig)
            p = bfs_matrix_goal(maze, vis, 1, 1, x, y, 51)
            if p is not None and len(p) <= 51:
                locations.add((x, y))

print(len(locations))




