from util.FileHelper import read_file_multiple_lines

p_dict = dict()
lines = read_file_multiple_lines('2021', 'day5')
for line in lines:
    [point1, point2] = line.strip().split(' -> ')
    p1_parts = point1.split(',')
    p2_parts = point2.split(',')
    x1 = int(p1_parts[0])
    y1 = int(p1_parts[1])
    x2 = int(p2_parts[0])
    y2 = int(p2_parts[1])
    # Diagonals
    if x1 != x2 and y1 != y2:
        y_add = True
        # Strategy is to use one loop over x and then increment or decrement y
        y = 0
        # set starting y to associated starting x based on min value
        if x1 < x2:
            y = y1
        else:
            y = y2
        # Figuring out whether to increment or decrement y
        # This if block is effectively checking if the start point has a higher y value than the end point
        if (x1 < x2 and y1 > y2) or (x2 < x1 and y2 > y1):
            y_add = False
        for x in range(min(x1, x2), max(x1, x2)+1):
            p_dict[(x, y)] = p_dict.get((x, y), 0) + 1
            if y_add:
                y += 1
            else:
                y -= 1
    elif x1 == x2:
        for y in range(min(y1, y2), max(y1, y2)+1):
            p_dict[(x1, y)] = p_dict.get((x1, y), 0) + 1
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2)+1):
            p_dict[(x, y1)] = p_dict.get((x, y1), 0) + 1

count = 0
for p in p_dict.values():
    if p >= 2:
        count += 1

print(count)
