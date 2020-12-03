puzzle_input = list()
with open('day3.txt', 'r') as f:
    puzzle_input = f.readlines()
    f.close()

height = len(puzzle_input)
width = len(puzzle_input[0]) - 1

def count_trees(slope_x, slope_y):
    cur_x = 0
    cur_y = 0
    tree_count = 0

    while cur_y < height:
        cur = puzzle_input[cur_y][cur_x]
        if (cur == '#'):
            tree_count += 1
        cur_y += slope_y
        cur_x = (cur_x + slope_x) % width

    return(tree_count)


def part1():
    return count_trees(3, 1)

def part2():
    running_mult = 1
    running_mult = running_mult * count_trees(1, 1)
    running_mult = running_mult * count_trees(3, 1)
    running_mult = running_mult * count_trees(5, 1)
    running_mult = running_mult * count_trees(7, 1)
    running_mult = running_mult * count_trees(1, 2)
    return running_mult

print(part1())
print(part2())