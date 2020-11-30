class node:
    def __init__(self, x, y):
        self.weight = 1
        self.children = None
        self.x = x
        self.y = y

class player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.attack = 3
        self.health = 200

data = list()
with open('day15.txt', 'r') as f:
    data = f.readlines()
    f.close()

for y in range(len(data)):
    x = 2
grid = [[data[y][x] for x in range(len(data[y]))] ]
