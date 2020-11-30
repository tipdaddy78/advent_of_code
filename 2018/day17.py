class clay:
    def __init__(self, n1, n2, n3, r):
        self.xval = None
        self.yval = None
        self.xmin = None
        self.xmax = None
        self.ymin = None
        self.ymax = None
        if r == 'x':
            self.yval = n1
            self.xmin = n2
            self.xmax = n3
        else:
            self.xval = n1
            self.ymin = n2
            self.ymax = n3

data = list()
with open('day17_test.txt', 'r') as f:
    data = f.readlines()
    f.close()

xmin = 100000
xmax = 0
ymin = 100000
ymax = 0
cd = list()
for d in data:
    parts = d.strip().split(',')
    n1 = int(parts[0].split('=')[1])
    n2 = int(parts[1].split('=')[1].split('..')[0])
    n3 = int(parts[1].split('=')[1].split('..')[1])
    if 'x' in parts[0]:
        c = clay(n1, n2, n3, 'y')
        cd.append(c)
        if  n1 > xmax:
            xmax = n1
        if n1 < xmin:
            xmin = n1
        if n2 < ymin:
            ymin = n2
        if n3 > ymax:
            ymax = n3
    else:
        c = clay(n1, n2, n3, 'x')
        cd.append(c)
        if  n1 > ymax:
            ymax = n1
        if n1 < ymin:
            ymin = n1
        if n2 < xmin:
            xmin = n2
        if n3 > xmax:
            xmax = n3

xmin -= 1
xmax += 1
ymin -= 1
grid = [['.' for x in range(xmin, xmax+1)] for y in range(ymin, ymax+1)]
water_x = 500 - xmin
grid[0][water_x] = '+'

for c in cd:
    if c.xval is not None:
        for y in range(c.ymin, c.ymax+1):
            grid[y-ymin][c.xval-xmin] = '#'
    else:
        for x in range(c.xmin, c.xmax+1):
            grid[c.yval-ymin][x-xmin] = '#'


def fill_board(board, x, y):
    if grid[y][x+1] == '.':
        board[y][x+1] = '|'
        fill_board(board, x+1, y)
    else:
        if grid[y-1][x] == '.':
            board[y][x]


flowing = True
cur_x = water_x
cur_y = 0
while flowing:
    flow_x = True
    flow_y = True
    while flow_y:
        if grid[cur_y + 1][cur_x] == '.':
            grid[cur_y + 1][cur_x] = '|'
            cur_y += 1
        elif  grid[cur_y + 1][cur_x] == '|':
            cur_y += 1
        elif (grid[cur_y-1][cur_x] == '#' or grid[cur_y-1][cur_x] == '~') and (grid[cur_y][cur_x-1] == '~' or grid[cur_y][cur_x-1] == '|') and grid[cur_y][cur_x+1] != '#':
            grid[cur_y][cur_x + 1] = '|'
            cur_x += 1
        else:
            flow_y = False
            while flow_x:
                if grid[cur_y][cur_x-1] == '.':
                    grid[cur_y][cur_x-1] = '~'
                    cur_x -= 1
                elif grid[cur_y][cur_x+1] == '~':
                    cur_x += 1
                elif (grid[cur_y][cur_x+1] == '.' or grid[cur_y][cur_x+1] == '|') and (grid[cur_y+1][cur_x+1] == '#' or grid[cur_y+1][cur_x+1] == '~'):
                    grid[cur_y][cur_x + 1] = '~'
                    cur_x += 1
                else:
                    flow_x = False






