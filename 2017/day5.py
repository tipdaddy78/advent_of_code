lines = list()
maze = list()
nbr_of_steps = 0
escaped = False

with open('day5.txt', 'r') as f:
    lines = f.readlines()
    f.close()

for line in lines:
    line = line.replace("\n", "")
    line = int(line)
    maze.append(line)

cur_pos = 0
while not escaped:
    nbr_of_steps += 1
    cur = maze[cur_pos]
    if cur >= 3:
        maze[cur_pos] -= 1
    else:
        maze[cur_pos] += 1
    cur_pos += cur
    if cur_pos >= len(maze):
        escaped = True

print(nbr_of_steps)