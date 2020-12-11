puzzle_input = list()
with open('day10.txt', 'r') as f:
    for l in f.readlines():
        puzzle_input.append(int(l.strip()))
    f.close()

puzzle_input.sort()

def part1():
    one_count = 0
    three_count = 0
    cur = 0
    for p in puzzle_input:
        if p - cur == 1:
            one_count += 1
        elif p - cur == 3:
            three_count += 1
        cur = p
    three_count += 1

    return one_count * three_count

print(part1())

def part2():
    adapters = puzzle_input
    adapters.insert(0, 0)
    adapters.insert(len(adapters), adapters[len(adapters) - 1] + 3)
    pow2 = 0
    pow7 = 0
    pow13 = 0
    i = 0
    while i < len(adapters) - 1:
        cur = adapters[i]
        cur_set = list()
        cur_set.append(adapters[i])
        for x in range(i+1, len(adapters)):
            comp = adapters[x]
            if adapters[x] - cur_set[len(cur_set) - 1] == 1:
                cur_set.append(adapters[x])
            else:
                if len(cur_set) == 3:
                    pow2 += 1
                elif len(cur_set) == 4:
                    pow2 += 2
                elif len(cur_set) == 5:
                    pow7 += 1
                elif len(cur_set) == 6:
                    pow13 += 1
                i = x
                break
    return pow(2, pow2) * pow(7, pow7) * pow(13, pow13)

print(part2())

