lines = list()
with open('day3.txt', 'r') as f:
    lines = f.readlines()
    f.close()

fabric = [([0] * 1000) for i in range (1000)] #Initialize matrix
overlaps = set()

for line in lines:
    split = line.split('@')
    id = int(split[0][1:].strip())
    start_l = int(split[1].split(":")[0].split(",")[0].strip())
    start_t = int(split[1].split(":")[0].split(",")[1].strip())
    width = int(split[1].split(":")[1].split("x")[0].strip())
    height = int(split[1].split(":")[1].split("x")[1].strip())

    for i in range(start_l, start_l + width):
        for j in range(start_t, start_t + height):
            if (fabric[i][j] == 0):
                fabric[i][j] = id
            else:
                overlaps.add(fabric[i][j])
                overlaps.add(id)
                fabric[i][j] = -1
count = 0
for i in range(1000):
    for j in range(1000):
        if (fabric[i][j] == -1):
            count += 1

for i in range(1, len(lines)):
    if i not in overlaps:
        print("ID: " + str(i) + " has no overlaps")

print(count)