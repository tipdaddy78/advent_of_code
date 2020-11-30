data = list()
with open('day10.txt', 'r') as f:
    data = f.readlines()
    f.close()

x_points = dict()
y_points = dict()
velocities = dict()
key = 0
ymin = 1000000
ymax = 0
xmin = 1000000
xmax = 0
for d in data:
    px = int(d[10:16])
    if px > xmax:
        xmax = px
    if px < xmin:
        xmin = px
    py = int(d[18:24])
    if py > ymax:
        ymax = py
    if py < ymin:
        ymin = py
    vx = int(d[36:38])
    vy = int(d[40:42])
    v = (vx, vy)
    x_points[key] = px
    y_points[key] = py
    velocities[key] = v
    key += 1

loop = True
i = 0
while loop:
    i += 1
    ymin = 1000000
    ymax = 0
    xmin = 1000000
    xmax = 0
    points = set()
    for key in x_points.keys():
        px = x_points.get(key)
        py = y_points.get(key)
        v = velocities.get(key)
        px += v[0]
        py += v[1]
        if px > xmax:
            xmax = px
        if px < xmin:
            xmin = px
        if py > ymax:
            ymax = py
        if py< ymin:
            ymin = py
        p = (px, py)
        points.add(p)
        x_points[key] = px
        y_points[key] = py

    if (xmax - xmin) * (ymax - ymin) <= 1000:
        for y in range(ymin, ymax+1):
            line = ''
            for x in range(xmin, xmax+1):
                p = (x, y)
                if p in points:
                    line += "X"
                else:
                    line += " "
            print(line)
            print(i)
            loop = False






