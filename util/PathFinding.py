from collections import deque as queue

# Direction vectors
dRow = [-1, 0, 1, 0]
dCol = [0, 1, 0, -1]


# Checks that x/y are inbounds
# Checks that it hasn't been to the point before.
# Checks that it isn't a wall (#)
def is_valid_bfs_matrix_goal(m, vis, x, y):
    if x < 0 or y < 0 or x >= len(m[0]) or y >= len(m):
        return False
    if vis[x][y]:
        return False
    if m[y][x] == '#':
        return False
    return True


# For 2D arrays of '.' and '#' matrices.  '.' = open, '#' = wall
# Returns the shortest path between start/goal or an empty list.
# Returns None if a path doesn't exist, or if taking more than the allowed max_steps
def bfs_matrix_goal(m, vis, start_x, start_y, goal_x, goal_y, max_steps=-1):
    q = queue()
    q.append([(start_x, start_y)])
    vis[start_x][start_y] = True

    if (start_x, start_y) == (goal_x, goal_y):
        return list()

    while len(q) > 0:
        path = q.popleft()
        cell = path[-1]
        x = cell[0]
        y = cell[1]
        # Terminate if going farther than max_steps steps
        # Doesn't return a path since it didn't reach the destination
        if max_steps != -1 and len(path) > max_steps:
            return None

        # Iterate over direction vectors to try going to adjacent cells
        for i in range(4):
            new_path = list(path)
            adjx = x + dRow[i]
            adjy = y + dCol[i]
            if is_valid_bfs_matrix_goal(m, vis, adjx, adjy):
                new_path.append((adjx, adjy))
                q.append(new_path)
                if (adjx, adjy) == (goal_x, goal_y):
                    return new_path
        vis[x][y] = True

    return None
