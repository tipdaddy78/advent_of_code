data = list()
with open('day12.txt', 'r') as f:
    data = f.readlines()
    f.close()

plant = data[0].split(":")[1].strip()





rules = data[2:]
baby_maker = dict()
for rule in rules:
    r = rule.split("=>")
    baby_maker[r[0].strip()] = r[1].strip()

init_state = '#.#####.#.#.####.####.#.#...#.......##..##.#.#.#.###..#.....#.####..#.#######.#....####.#....##....#'

def sum_plants(curr):
   diff = (len(curr) - 100) // 2
   sum = 0
   for i, c in enumerate(curr):
      if c == '#':
         sum += (i - diff)
   return sum

curr = init_state
prev_sum = sum_plants(init_state)
diffs = []
num_iters = 110
for i in range(num_iters):
    if(i == 20):
        print("Part 1: " + str(sum_plants(curr)))
    curr = "...." + curr + "...."
    next = ""
    for x in range(2, len(curr) - 2):
        sub = curr[x-2:x+3]
        next+= baby_maker.get(sub)
    curr = next
    currsum = sum_plants(curr)
    diff = currsum - prev_sum
    diffs.append(diff)
    if(len(diffs) > 100): diffs.pop(0)
    prev_sum = currsum

last100diff = sum(diffs) // len(diffs)

total = (50000000000 - num_iters) * last100diff + sum_plants(curr)

print("Part 2: " + str(total))

