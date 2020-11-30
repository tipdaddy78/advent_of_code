class node:
    def __init__(self, num_c):
        self.num_c = num_c
        self.num_m = None
        self.children = list()
        self.meta = list()

    def setNumM(self, num_m):
        self.num_m = num_m

    def addChild(self, node):
        self.children.append(node)

    def addMeta(self, meta):
        self.meta.append(meta)

    def getValue(self):
        value = 0
        if self.num_c == 0:
            for m in self.meta:
                value += m
        else:
            for m in self.meta:
                if m <= self.num_c:
                    value += self.children[m-1].getValue()
        return value

def makeNode(data, i):
    n = node(int(data[i]))
    i += 1
    n.setNumM(int(data[i]))
    i += 1
    while len(n.children) != n.num_c:
        c = makeNode(data, i)
        n.addChild(c[0])
        i = c[1]
    while len(n.meta) != n.num_m:
        n.addMeta(int(data[i]))
        i += 1
    return (n, i)


data = list()
with open('day8.txt', 'r') as f:
    data = f.read().strip().split(' ')
    f.close()

root = makeNode(data, 0)[0]
print(root.getValue())
x = 2