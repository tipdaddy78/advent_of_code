wires = list()
with open('day3.txt', 'r') as f:
    wires = f.readlines()
    f.close()

wire1_steps = dict()
wire2_steps = dict()

wire1 = wires[0].strip().split(',')
wire2 = wires[1].strip().split(',')

x = 0
y = 0
steps = 0

for step in wire1:
    d = step[0]
    v = int(step[1:])
    if d == 'R':
        for i in range(v):
            steps += 1
            x += 1
            wire1_steps[(x, y)] = steps
    elif d == 'L':
        for i in range(v):
            steps += 1
            x -= 1
            wire1_steps[(x, y)] = steps
    elif d == 'U':
        for i in range(v):
            steps += 1
            y += 1
            wire1_steps[(x, y)] = steps
    elif d == 'D':
        for i in range(v):
            steps += 1
            y -= 1
            wire1_steps[(x, y)] = steps


x = 0
y = 0
steps = 0

for step in wire2:
    d = step[0]
    v = int(step[1:])
    if d == 'R':
        for i in range(v):
            steps += 1
            x += 1
            wire2_steps[(x, y)] = steps
    elif d == 'L':
        for i in range(v):
            steps += 1
            x -= 1
            wire2_steps[(x, y)] = steps
    elif d == 'U':
        for i in range(v):
            steps += 1
            y += 1
            wire2_steps[(x, y)] = steps
    elif d == 'D':
        for i in range(v):
            steps += 1
            y -= 1
            wire2_steps[(x, y)] = steps

intersection_points = dict()

for point in wire1_steps:
    if point in wire2_steps:
        if point in intersection_points:
            continue
        else:
            intersection_points[point] = wire1_steps[point] + wire2_steps[point]

lowest = 10000000000000000000000000000000000000000000000
for point in intersection_points:
    if intersection_points[point] < lowest:
        lowest = intersection_points[point]

print(lowest)

