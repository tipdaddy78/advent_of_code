def manhattan_distance(ax, ay, bx, by):
    return abs(ax - bx) + abs(ay - by)

coords = list()
with open('day6.txt', 'r') as f:
    coords = f.readlines()
    f.close()

c_dict = dict()
idx = 0
x_max = 0
y_max = 0
for c in coords:
    p = c.strip().split(',')
    point = (int(p[0].strip()), int(p[1].strip()))
    c_dict[idx] = point
    if point[0] > x_max:
        x_max = point[0]
    if point[1] > y_max:
        y_max = point[1]
    idx += 1

x_max += 1
y_max += 1

grid = [[-1 for y in range(y_max)] for x in range(x_max)]
regions = dict()
big_area = 0
for x in range(x_max-1):
    for y in range(y_max-1):
        best = x_max + y_max
        bestNum = -1
        totalDist = 0
        for key in c_dict.keys():
            p = c_dict.get(key)
            dist = manhattan_distance(x, y, p[0], p[1])
            if dist < best:
                best = dist
                bestNum = key
            elif dist == best:
                bestNum = -1
            totalDist += dist
        if totalDist < 10000:
            big_area += 1

        grid[x][y] = bestNum
        total = regions.get(bestNum)
        if total == None:
            total = 1
        else:
            total += 1
        regions[bestNum] = total


for x in range(x_max):
    bad = grid[x][0]
    regions[bad] = 0
    bad = grid[x_max-1][0]
    regions[bad] = 0

for y in range(y_max):
    bad = grid[0][y]
    regions[bad] = 0
    bad = grid[x_max-1][y]
    regions[bad] = 0

biggest = 0
for size in regions.values():
    if size > biggest:
        biggest = size

print(biggest)
print(big_area)



