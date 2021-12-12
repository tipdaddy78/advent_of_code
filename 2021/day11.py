from util.FileHelper import read_file_multiple_lines

data = read_file_multiple_lines('2021', 'day11')
octopuses = dict()

# Data collection
for y in range(len(data)):
    for x in range(len(data[y].strip())):
        octopuses[(x, y)] = int(data[y][x])


def get_neighbors(start_x, start_y):
    dx = [1, 1, 0, -1, -1, -1, 0, 1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    neighbors = list()
    for i in range(len(dx)):
        neighbors.append((start_x+dx[i], start_y+dy[i]))
    return neighbors


def flash(flashed_set, octopus_dict, octos_to_flash):
    flashed_set = flashed_set.union(octos_to_flash)
    for octo_to_flash in octos_to_flash:
        to_flash = set()
        flashed_set.add(octo_to_flash)
        neighbors = get_neighbors(octo_to_flash[0], octo_to_flash[1])
        for neighbor in neighbors:
            if neighbor in octopus_dict:
                octopus_dict[neighbor] += 1
                if neighbor not in flashed_set:
                    if octopus_dict[neighbor] > 9:
                        to_flash.add(neighbor)
        if len(to_flash) > 0:
            flashed_set, octopus_dict = flash(flashed_set, octopus_dict, to_flash)
    return flashed_set, octopus_dict


flashes = 0
n = 0
while True:
    n += 1
    flashed = set()
    round_to_flash = set()
    for o in octopuses.keys():
        octopuses[o] += 1
        if octopuses[o] > 9:
            round_to_flash.add(o)
    if len(round_to_flash) > 0:
        flashed, octopuses = flash(flashed, octopuses, round_to_flash)
    flashes += len(flashed)
    # Part 2
    if len(flashed) == len(octopuses.keys()):
        print("Part 2:", n)
        break
    for f in flashed:
        octopuses[f] = 0
    if n == 99:
        print("Part 1:", flashes, "flashes")

print(flashes)
