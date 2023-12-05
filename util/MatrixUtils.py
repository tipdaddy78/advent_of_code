# Returns a list of tuples points neighboring this one in 2D space
# This version of the function assumes an infinite size grid
# Visual Example:
#       In the grid below, the point defined by (x, y) is listed as _
#       Neighbors are listed as #
#       All other points are listed as .
#
#       . . . . .
#       . # # # .
#       . # _ # .
#       . # # # .
#       . . . . .
def get_2d_neighbor_points(x, y):
    return get_2d_neighbor_points_bounded(x, y, None, None, None, None)


# Overloading method to allow both bounded and unbounded method.
# When a value exists here, neighbors won't be returned if they are outside those bounds
# Returns a list of tuples of neighbors within the bounds
# Visual Examples:
#       In the grids below, the point defined by (x, y) is listed as _
#       Neighbors are listed as #
#       All other points are listed as .
#
#       _ # . . .
#       # # . . .
#       . . . . .
#       . . . . .
#       . . . . .
#
#       . # _ # .
#       . # # # .
#       . . . . .
#       . . . . .
#       . . . . .
#
#       . . . . .
#       . . . # #
#       . . . # _
#       . . . # #
#       . . . . .
#
#       . . . . .
#       . . . . .
#       . . . . .
#       . # # # .
#       . # _ # .
#
#       . . . . .
#       # # . . .
#       _ # . . .
#       # # . . .
#       . . . . .
def get_2d_neighbor_points_bounded(x, y, x_min, y_min, x_max, y_max):
    neighbors = list()
    if x_min is None or (x - 1) >= x_min:

        # Up/Left neighbor
        if y_min is None or (y - 1) >= y_min:
            neighbors.append((x - 1, y - 1))

        # Left neighbor
        neighbors.append((x - 1, y))

        # Down/Left neighbor
        if y_max is None or (y + 1) <= y_max:
            neighbors.append((x - 1, y + 1))

    # Up neighbor
    if y_min is None or (y - 1) >= y_min:
        neighbors.append((x, y - 1))

    # Down neighbor
    if y_max is None or (y + 1) <= y_max:
        neighbors.append((x, y + 1))

    if x_max is None or (x + 1) <= x_max:

        # Up/Right neighbor
        if y_min is None or (y - 1) >= y_min:
            neighbors.append((x + 1, y - 1))

        # Right neighbor
        neighbors.append((x + 1, y))

        # Down/Right neighbor
        if y_max is None or (y + 1) <= y_max:
            neighbors.append((x + 1, y + 1))

    return neighbors
