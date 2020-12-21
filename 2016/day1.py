input = ""

with open('day1.txt', 'r') as f:
    input = f.read()
    f.close()

instructions = input.split(',')
x = 0
y = 0
cur_dir = 'n'

for i in instructions:
    i = i.strip()

    #update current direction
    if cur_dir == 'n':
        if i[0] == 'L':
            cur_dir = 'w'
        elif i[0] == 'R':
            cur_dir = 'e'
    elif cur_dir == 'w':
        if i[0] == 'L':
            cur_dir = 's'
        elif i[0] == 'R':
            cur_dir = 'n'
    elif cur_dir == 's':
        if i[0] == 'L':
            cur_dir = 'e'
        elif i[0] == 'R':
            cur_dir = 'w'
    elif cur_dir == 'e':
        if i[0] == 'L':
            cur_dir = 'n'
        elif i[0] == 'R':
            cur_dir = 's'

    if cur_dir == 'n':
        y += int(i[1])
    elif cur_dir == 'w':
        x -= int(i[1])
    elif cur_dir == 's':
        y -= int(i[1])
    elif cur_dir == 'e':
        x += int(i[1])

print(x, y)
