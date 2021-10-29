from util.FileHelper import *

inputLine = read_file_single_line("2016", "day1")
visited = set()

instructions = inputLine.split(',')
x = 0
y = 0
cur_dir = 'n'
visited.add((x, y))
factory_found = False

for i in instructions:
    i = i.strip()
    match cur_dir:
        case 'n':
            if i[0] == 'L':
                cur_dir = 'w'
            elif i[0] == 'R':
                cur_dir = 'e'
        case 'w':
            if i[0] == 'L':
                cur_dir = 's'
            elif i[0] == 'R':
                cur_dir = 'n'
        case 's':
            if i[0] == 'L':
                cur_dir = 'e'
            elif i[0] == 'R':
                cur_dir = 'w'
        case 'e':
            if i[0] == 'L':
                cur_dir = 'n'
            elif i[0] == 'R':
                cur_dir = 's'
    for j in range(int(i[1:])):
        match cur_dir:
            case 'n':
                y += 1
            case 'w':
                x -= 1
            case 's':
                y -= 1
            case 'e':
                x += 1
        cur_size = len(visited)
        visited.add((x, y))
        if cur_size == len(visited) and not factory_found:
            print('Factory is at: ' + str((x, y)))
            factory_found = True

print(x, y)
