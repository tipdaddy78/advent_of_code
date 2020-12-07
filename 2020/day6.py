puzzle_input = list()
with open('day6.txt', 'r') as f:
    puzzle_input = f.readlines()
    f.close()

def process():
    part1 = 0
    part2 = 0
    cur = dict()
    group = 0
    for line in puzzle_input:
        if line.strip() == '':
            part1 += len(cur.keys())
            for k in cur.keys():
                if cur[k] == group:
                    part2 += 1
            cur = dict()
            group = 0
        else:
            group += 1
            for c in line.strip():
                if c in cur.keys():
                    cur[c] = cur[c] + 1
                else:
                    cur[c] = 1
    #add last group
    part1 += len(cur.keys())
    for k in cur.keys():
        if cur[k] == group:
            part2 += 1
    print(part1)
    print(part2)


process()
