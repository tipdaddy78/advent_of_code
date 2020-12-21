def getPowerLevel(x, y, s):
    rackID = x + 10
    powerLevel = rackID * y
    powerLevel += s
    powerLevel *= rackID
    p = str(powerLevel)
    powerLevel = 0
    if len(p) >= 3:
        powerLevel = int(p[len(p)-3])
    powerLevel -= 5
    return powerLevel

grid = [[0 for x in range(300)] for y in range(300)]
s = 8141

for x in range(300):
    for y in range(300):
        grid[x][y] = getPowerLevel(x+1, y+1, s)

max = 0
x_max = 0
y_max = 0
max_size = 0
sq_size = 1

while sq_size <= 300:
    for x in range(300-(sq_size-1)):
        for y in range(300-(sq_size-1)):
            cur = 0
            for dx in range(sq_size):
                for dy in range(sq_size):
                    cur += grid[x+dx][y+dy]
            if cur > max:
                max = cur
                x_max = x
                y_max = y
                max_size = sq_size
    sq_size += 1

print(x_max+1)
print(y_max+1)
print(max_size)

