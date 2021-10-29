from util.FileHelper import read_file_multiple_lines

directions = read_file_multiple_lines('2015', 'day6')


def take_action(min_x, min_y, max_x, max_y, a, onOff, bright):
    for y in range(int(min_y), int(max_y) + 1):
        for x in range(int(min_x), int(max_x) + 1):
            if a == 'toggle':
                onOff[(x, y)] = not onOff[(x, y)]
                bright[(x, y)] += 2
            elif a == 'turn on':
                onOff[(x, y)] = True
                bright[(x, y)] += 1
            else:
                onOff[(x, y)] = False
                if bright[(x, y)] != 0:
                    bright[(x, y)] -= 1


def process():
    grid = dict()
    brightness = dict()
    for y in range(1000):
        for x in range(1000):
            brightness[(x, y)] = 0
            grid[(x, y)] = False
    for d in directions:
        parts = d.split(' ')
        if parts[0] == 'turn':
            mins = parts[2].split(',')
            maxs = parts[4].strip().split(',')
            take_action(mins[0], mins[1], maxs[0], maxs[1], str(parts[0] + ' ' + parts[1]), grid, brightness)
        else:
            mins = parts[1].split(',')
            maxs = parts[3].strip().split(',')
            take_action(mins[0], mins[1], maxs[0], maxs[1], parts[0], grid, brightness)
    count = 0
    count2 = 0
    for key in grid.keys():
        if grid.get(key):
            count += 1
        count2 += brightness.get(key)

    print(count)
    print(count2)

process()