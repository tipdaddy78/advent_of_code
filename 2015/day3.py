from util.FileHelper import read_file_single_line

directions = read_file_single_line('2015', 'day3')

houses = set()
x = 0
y = 0
houses_2 = set()
s_x = 0
r_x = 0
s_y = 0
r_y = 0
for i in range(len(directions)):
    houses.add((x, y))
    houses_2.add((r_x, r_y))
    houses_2.add((s_x, s_y))
    d = directions[i]
    if d == '^':
        y += 1
    elif d == '>':
        x += 1
    elif d == '<':
        x -= 1
    elif d == 'v':
        y -= 1
    if i % 2 == 0:
        if d == '^':
            s_y += 1
        elif d == '>':
            s_x += 1
        elif d == '<':
            s_x -= 1
        elif d == 'v':
            s_y -= 1
    else:
        if d == '^':
            r_y += 1
        elif d == '>':
            r_x += 1
        elif d == '<':
            r_x -= 1
        elif d == 'v':
            r_y -= 1

print(len(houses))
print(len(houses_2))