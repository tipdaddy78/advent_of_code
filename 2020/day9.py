puzzle_input = list()
with open('day9.txt', 'r') as f:
    puzzle_input = f.readlines()
    f.close()

def part1():
    preamble = puzzle_input[0:25]
    found = False
    for i in range(25, len(puzzle_input)):
        cur = int(puzzle_input[i].strip())
        found = False
        for x in range(len(preamble)):
            for y in range(x + 1, len(preamble)):
                if not found:
                    if int(preamble[x].strip()) + int(preamble[y].strip()) == cur:
                        preamble.pop(0)
                        preamble.append(str(cur))
                        found = True
                        break
            if found:
                break
        if not found:
            return cur
    return -1

def part2(target):
    cur = 0
    group = list()
    for x in range(len(puzzle_input)):
        cur = 0
        group = list()
        for y in range(x, len(puzzle_input)):
            cur += int(puzzle_input[y].strip())
            group.append(int(puzzle_input[y].strip()))
            if cur == target:
                group.sort()
                return(group[0] + group[len(group) - 1])
            elif cur < target:
                continue
            else:
                break
    return -1

target = part1()
print(target)
print(part2(target))

