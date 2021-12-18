intcodes = dict()
input_val = 1

with open('input/day11.txt', 'r') as f:
    data = f.read()
    string_codes = data.strip().split(',')
    for c in range(len(string_codes)):
        intcodes[c] = int(string_codes[c])
    f.close()

hull = dict()
robot_position = (0, 0)
hull[robot_position] = True
robot_direction = 'U'
paintMode = True
minX = 100000000000000000
minY = 100000000000000000
maxX = 0
maxY = 0

position = 0
relative_base = 0
while intcodes[position] != 99:
    op_code = intcodes[position]
    e = 0
    if (position + 1) in intcodes.keys():
        b = intcodes[position + 1]
    else:
        b = 0
    if (position + 2) in intcodes.keys():
        c = intcodes[position + 2]
    else:
        c = 0
    if (position + 3) in intcodes.keys():
        d = intcodes[position + 3]
    else:
        d = 0
    if op_code == 1:
        if b in intcodes.keys():
            op1 = intcodes[b]
        else:
            op1 = 0
        if c in intcodes.keys():
            op2 = intcodes[c]
        else:
            op2 = 0
        e = op1 + op2
        intcodes[d] = e
        position += 4
    elif op_code == 2:
        if b in intcodes.keys():
            op1 = intcodes[b]
        else:
            op1 = 0
        if c in intcodes.keys():
            op2 = intcodes[c]
        else:
            op2 = 0
        e = op1 * op2
        intcodes[d] = e
        position += 4
    elif op_code == 3:
        cur_panel = hull.get(robot_position)
        if (cur_panel == None) or cur_panel == False:
            input_val = 0
        else:
            input_val = 1
        intcodes[b] = input_val
        position += 2
    elif op_code == 4:
        if b in intcodes.keys():
            op1 = intcodes[b]
        else:
            op1 = 0
        print(op1)
        if paintMode:
            if op1 == 0:
                hull[robot_position] = False
            else:
                hull[robot_position] = True
        else:
            if op1 == 0: #turn LEFT
                if robot_direction == 'U':
                    robot_direction = 'L'
                elif robot_direction == 'L':
                    robot_direction = 'D'
                elif robot_direction == 'D':
                    robot_direction = 'R'
                else:
                    robot_direction = 'U'
            else: #turn RIGHT
                if robot_direction == 'U':
                    robot_direction = 'R'
                elif robot_direction == 'L':
                    robot_direction = 'U'
                elif robot_direction == 'D':
                    robot_direction = 'L'
                else:
                    robot_direction = 'D'
            if robot_direction == 'U':
                new_robot_position = (robot_position[0], robot_position[1] + 1)
            elif robot_direction == 'L':
                new_robot_position = (robot_position[0] - 1, robot_position[1])
            elif robot_direction == 'D':
                new_robot_position = (robot_position[0], robot_position[1] - 1)
            else:
                new_robot_position = (robot_position[0] + 1, robot_position[1])
            robot_position = new_robot_position
            if robot_position[0] > maxX:
                maxX = robot_position[0]
            if robot_position[0] < minX:
                minX = robot_position[0]
            if robot_position[1] > maxY:
                maxY = robot_position[1]
            if robot_position[1] < minY:
                minY = robot_position[1]
        paintMode = not paintMode
        position += 2
    elif op_code == 5:
        if b in intcodes.keys():
            op1 = intcodes[b]
        else:
            op1 = 0
        if c in intcodes.keys():
            op2 = intcodes[c]
        else:
            op2 = 0
        if op1 != 0:
            position = op2
        else:
            position += 3
    elif op_code == 6:
        if b in intcodes.keys():
            op1 = intcodes[b]
        else:
            op1 = 0
        if c in intcodes.keys():
            op2 = intcodes[c]
        else:
            op2 = 0
        if op1 == 0:
            position = op2
        else:
            position += 3
    elif op_code == 7:
        if b in intcodes.keys():
            op1 = intcodes[b]
        else:
            op1 = 0
        if c in intcodes.keys():
            op2 = intcodes[c]
        else:
            op2 = 0
        if op1 < op2:
            intcodes[d] = 1
        else:
            intcodes[d] = 0
        position += 4
    elif op_code == 8:
        if b in intcodes.keys():
            op1 = intcodes[b]
        else:
            op1 = 0
        if c in intcodes.keys():
            op2 = intcodes[c]
        else:
            op2 = 0
        if op1 == op2:
            intcodes[d] = 1
        else:
            intcodes[d] = 0
        position += 4
    elif op_code == 9:
        if b in intcodes.keys():
            op1 = intcodes[b]
        else:
            op1 = 0
        relative_base += op1
        position += 2
    else: #Parameter Modes
        str_op = str(op_code)[::-1]
        param_op = int(str_op[0])
        b_mode = 0
        c_mode = 0
        d_mode = 0
        for i in range(2, len(str_op)):
            if i == 2:
                b_mode = int(str_op[i])
            elif i == 3:
                c_mode = int(str_op[i])
            elif i == 4:
                d_mode = int(str_op[i])

        op1 = -1
        op2 = -1
        op3 = -1
        if b_mode == 0:
            if b in intcodes.keys():
                op1 = intcodes[b]
            else:
                op1 = 0
        elif b_mode == 1:
            op1 = b
        else:
            if (b + relative_base) in intcodes.keys():
                op1 = intcodes[b + relative_base]
            else:
                op1 = 0
        if param_op != 3 and param_op != 4 and param_op != 9:
            if c_mode == 0:
                if c in intcodes.keys():
                    op2 = intcodes[c]
                else:
                    op2 = 0
            elif c_mode == 1:
                op2 = c
            else:
                if (c + relative_base) in intcodes.keys():
                    op2 = intcodes[c + relative_base]
                else:
                    op2 = 0
        if param_op == 1:
            e = op1 + op2
            if d_mode == 0:
                intcodes[d] = e
            elif d_mode == 2:
                intcodes[d + relative_base] = e
            position += 4
        elif param_op == 2:
            e = op1 * op2
            if d_mode == 0:
                intcodes[d] = e
            elif d_mode == 2:
                intcodes[d + relative_base] = e
            position += 4
        elif param_op == 3:
            cur_panel = hull.get(robot_position)
            if (cur_panel == None) or cur_panel == False:
                input_val = 0
            else:
                input_val = 1
            if b_mode == 0:
                intcodes[b] = input_val
            else:
                intcodes[b + relative_base] = input_val
            position += 2
        elif param_op == 4:
            print(op1)
            if paintMode:
                if op1 == 0:
                    hull[robot_position] = False
                else:
                    hull[robot_position] = True
            else:
                if op1 == 0:  # turn LEFT
                    if robot_direction == 'U':
                        robot_direction = 'L'
                    elif robot_direction == 'L':
                        robot_direction = 'D'
                    elif robot_direction == 'D':
                        robot_direction = 'R'
                    else:
                        robot_direction = 'U'
                else:  # turn RIGHT
                    if robot_direction == 'U':
                        robot_direction = 'R'
                    elif robot_direction == 'L':
                        robot_direction = 'U'
                    elif robot_direction == 'D':
                        robot_direction = 'L'
                    else:
                        robot_direction = 'D'
                if robot_direction == 'U':
                    new_robot_position = (robot_position[0], robot_position[1] + 1)
                elif robot_direction == 'L':
                    new_robot_position = (robot_position[0] - 1, robot_position[1])
                elif robot_direction == 'D':
                    new_robot_position = (robot_position[0], robot_position[1] - 1)
                else:
                    new_robot_position = (robot_position[0] + 1, robot_position[1])
                robot_position = new_robot_position
                if robot_position[0] > maxX:
                    maxX = robot_position[0]
                if robot_position[0] < minX:
                    minX = robot_position[0]
                if robot_position[1] > maxY:
                    maxY = robot_position[1]
                if robot_position[1] < minY:
                    minY = robot_position[1]
            paintMode = not paintMode
            position += 2
        elif param_op == 5:
            if op1 != 0:
                position = op2
            else:
                position += 3
        elif param_op == 6:
            if op1 == 0:
                position = op2
            else:
                position += 3
        elif param_op == 7:
            if op1 < op2:
                if d_mode == 0:
                    intcodes[d] = 1
                elif d_mode == 2:
                    intcodes[d + relative_base] = 1
            else:
                if d_mode == 0:
                    intcodes[d] = 0
                elif d_mode == 2:
                    intcodes[d + relative_base] = 0
            position += 4
        elif param_op == 8:
            if op1 == op2:
                if d_mode == 0:
                    intcodes[d] = 1
                elif d_mode == 2:
                    intcodes[d + relative_base] = 1
            else:
                if d_mode == 0:
                    intcodes[d] = 0
                elif d_mode == 2:
                    intcodes[d + relative_base] = 0
            position += 4
        elif param_op == 9:
            relative_base += op1
            position += 2

grid = [['.' for x in range(minX, maxX + 1)] for y in range(minY, maxY + 1)]
print(hull)
x = 0
y = 0
for j in range(len(grid) + 1):
    for i in range(len(grid[0])):
        tup = (x, y)
        if tup in hull.keys():
            if hull.get(tup):
                grid[j][i] = '#'
        x += 1
    x = 0
    y -= 1

for r in range(len(grid)):
    print(grid[r])

