directions = list()

with open('day11.txt', 'r') as f:
    directions = f.read().strip().split(',')
    f.close()

def at_start(x, y):
    return x == 0 and y == 0

def find_distance_to_start(b_x, b_y):
    return ((b_x)**2 + (b_y)**2)**0.5

def find_steps_home(x, y):
    dirs = ['n', 's', 'nw', 'sw', 'ne', 'se']
    steps = 0
    min = 1000000000000000000000000000000000000000000000000000000000000000000000000
    min_dir = ''
    while not at_start(x, y):
        for d in dirs:
            if d == "n":
                dist = find_distance_to_start(x, y - 1)
                if dist < min:
                    min = dist
                    min_dir = d
            elif d == "s":
                dist = find_distance_to_start(x, y + 1)
                if dist < min:
                    min = dist
                    min_dir = d
            elif d == "nw":
                dist = find_distance_to_start(x - 1, y - 0.5)
                if dist < min:
                    min = dist
                    min_dir = d
            elif d == "sw":
                dist = find_distance_to_start(x - 1, y + 0.5)
                if dist < min:
                    min = dist
                    min_dir = d
            elif d == "ne":
                dist = find_distance_to_start(x + 1, y - 0.5)
                if dist < min:
                    min = dist
                    min_dir = d
            elif d == "se":
                dist = find_distance_to_start(x + 1, y + 0.5)
                if dist < min:
                    min = dist
                    min_dir = d
        if min_dir == "n":
            y -= 1
        elif min_dir == "s":
            y += 1
        elif min_dir == "nw":
            y -= 0.5
            x -= 1
        elif min_dir == "sw":
            y += 0.5
            x -= 1
        elif min_dir == "ne":
            y -= 0.5
            x += 1
        elif min_dir == "se":
            y += 0.5
            x += 1
        steps += 1
    return steps

x = 0
y = 0
max_steps = 0

for d in directions:
    if d == "n":
        y -= 1
        steps = find_steps_home(x, y)
        if steps > max_steps:
            max_steps = steps
    elif d == "s":
        y += 1
        steps = find_steps_home(x, y)
        if steps > max_steps:
            max_steps = steps
    elif d == "nw":
        y -= 0.5
        x -= 1
        steps = find_steps_home(x, y)
        if steps > max_steps:
            max_steps = steps
    elif d == "sw":
        y += 0.5
        x -= 1
        steps = find_steps_home(x, y)
        if steps > max_steps:
            max_steps = steps
    elif d == "ne":
        y -= 0.5
        x += 1
        steps = find_steps_home(x, y)
        if steps > max_steps:
            max_steps = steps
    elif d == "se":
        y += 0.5
        x += 1
        steps = find_steps_home(x, y)
        if steps > max_steps:
            max_steps = steps

print(find_steps_home(x, y))
print(max_steps)