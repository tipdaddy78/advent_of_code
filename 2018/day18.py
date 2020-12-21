data = list()
with open('day18.txt', 'r') as f:
    data = f.readlines()
    f.close()

class node:
    def __init__(self, location, value, neighbors):
        self.value = value
        self.neighbors = neighbors
        self.location = location

    def setValue(self, value):
        self.value = value

def open_to_tree(neighbors, board):
    count = 0
    for n in neighbors:
        if board.get(n).value == '|':
            count += 1
            if count == 3:
                return True
    return False

def tree_to_lumber(neighbors, board):
    count = 0
    for n in neighbors:
        if board.get(n).value == '#':
            count += 1
            if count == 3:
                return True
    return False

def lumber_remain_lumber(neighbors, board):
    hasTree = False
    hasLumber = False
    for n in neighbors:
        if board.get(n).value == '#':
            if not hasLumber:
                hasLumber = True
        if board.get(n).value == '|':
            if not hasTree:
                hasTree = True
        if hasTree and hasLumber:
            return True
    return False

board = dict()
ymax = len(data)
xmax = len(data[0].strip())
for y in range(len(data)):
    for x in range(len(data[y].strip())):
        key = (x, y)
        neighbors = set()
        if x > 0:
            neighbors.add((x-1, y))
            if y > 0:
                neighbors.add((x-1, y-1))
            if y < ymax-1:
                neighbors.add((x-1, y+1))
        if y > 0:
            neighbors.add((x, y-1))
        if y < ymax-1:
            neighbors.add((x, y+1))
        if x < xmax-1:
            neighbors.add((x+1, y))
            if y > 0:
                neighbors.add((x+1, y-1))
            if y < ymax-1:
                neighbors.add((x+1, y+1))
        n = node(key, data[y][x], neighbors)
        board[key] = n


diffs = []
prev_diffs = []
cur = 0
num_iters = 6000
tree_count = 0
lumber_count = 0
open_count = 0

for t in range(1000000000):
    cur += 1
    new_board = dict()
    prev_diffs = diffs
    new_diffs = list()
    for d in diffs:
        new_diffs.append(d)
    tree_count = 0
    lumber_count = 0
    open_count = 0
    for k in board.keys():
        n = board.get(k)
        val = ''
        neighs = n.neighbors
        if n.value == '|':
            if tree_to_lumber(neighs, board):
                val = '#'
                lumber_count += 1
            else:
                val = '|'
                tree_count += 1
        if n.value == '#':
            if not lumber_remain_lumber(neighs, board):
                val = '.'
                open_count += 1
            else:
                val = '#'
                lumber_count += 1
        if n.value == '.':
            if open_to_tree(neighs, board):
                val = '|'
                tree_count += 1
            else:
                val = '.'
                open_count += 1
        n2 = node(k, val, neighs)
        new_board[k] = n2



    for y in range(ymax):
        line = ''
        for x in range(xmax):
            t = (x,y)
            n = new_board.get(t)
            line += n.value
        print(line)
    board = new_board
    print('')
    v = tree_count * lumber_count
    new_diffs.append(v)
    if (len(new_diffs) > 28): new_diffs.pop(0)
    if len(new_diffs) == 28 and len(prev_diffs) == 28:
        sorted_prev = sorted(prev_diffs)
        sorted_diffs = sorted(new_diffs)
        if sorted_prev == sorted_diffs:
            break
    diffs = new_diffs


total = new_diffs[((1000000000 - cur) % 28) - 1]

print(total)




