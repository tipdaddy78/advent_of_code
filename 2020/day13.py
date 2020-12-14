puzzle_input = list()
with open('day13.txt', 'r') as f:
    for l in f.readlines():
        puzzle_input.append(l.strip())
    f.close()

earliest = int(puzzle_input[0])
bus_ids = list()
bus_tups = list()
c = 0
first = 0
for b in puzzle_input[1].split(','):
    if b != 'x':
        bus_ids.append(int(b))
        bus_tups.append((int(b), c))
    if c == 0:
        first = int(b)
    c += 1

def part1(e, buses):
    start = e
    bus = 0
    cur = e
    found = False
    while True:
        for b in buses:
            if cur % b == 0:
                bus = b
                found = True
                break
        if found:
            break
        else:
            cur += 1
    dur =  cur - start
    return bus * dur

def part2(busses):
    lcm = 1
    time = 0
    for i in range(len(busses) - 1):
        bus = busses[i+1][0]
        offset = busses[i+1][1]
        lcm *= busses[i][0]
        while (time + offset) % bus != 0:
            time += lcm
    return time


print(part1(earliest, bus_ids))
print(part2(bus_tups))
