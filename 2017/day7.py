class Tower:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.children = None
        self.parent = None

    def add_support(self, support):
        self.children.append(support)

    def set_parent(self, parent):
        self.parent = parent

    def print(self):
        print(self.name, "(" + str(self.weight) + ")", " supports:")
        print("\t", self.children)

    def is_leaf(self):
        if len(self.children) == 0:
            return True
        else:
            return False

    def get_weight(self):
        if self.is_leaf():
            return self.weight
        else:


lines = list()
towers = dict()

with open('day7.txt', 'r') as f:
    lines = f.readlines()
    f.close()

for line in lines:
    line = line.replace("\n", "")
    elements = line.split(" ")
    t_name = elements[0]
    t_weight = int(elements[1].replace("(", "").replace(")", ""))

    t_tower = Tower(t_name, t_weight)
    if '->' in line:
        for i in range(3, len(elements)):
            t_support = elements[i].replace(',', '')
            t_tower.add_support(t_support)

    towers[t_tower.name] = t_tower

for tower in towers:
    for child in towers.get(tower).children:
        child_tower = towers.get(child)
        child_tower.set_parent(tower)


