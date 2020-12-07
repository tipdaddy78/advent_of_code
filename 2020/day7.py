puzzle_input = list()
with open('day7.txt', 'r') as f:
    puzzle_input = f.readlines()
    f.close()

bags = dict()

class Bag:
    def __init__(self):
        self.id = ''
        self.children = list()

    def set_id(self, id):
        self.id = id

    def add_child(self, child):
        self.children.append(child)

    def has_child(self, id):
        for c in self.children:
            if id in c:
                return True
        return False


for p in puzzle_input:
    parts = p.strip().split('bags contain')
    children = parts[1].replace('.', '').replace('bags', '').replace('bag', '').split(',')
    b = Bag()
    b.set_id(parts[0].strip())
    for c in children:
        if c.strip() != 'no other':
            b.add_child(c.strip())
    bags[b.id] = b

def part1():
    keys = list()
    key_set = set()
    keys.append('shiny gold')
    total = 0
    while len(keys) > 0:
        for k in bags.keys():
            bag = bags[k]
            if bag.id in key_set:
                continue
            if bag.has_child(keys[0]):
                if bag.id not in keys:
                    key_set.add(bag.id)
                    keys.append(bag.id)
                    total += 1
        keys.pop(0)
    return total

def get_bag_total(target_id):
    bag = bags.get(target_id)
    if len(bag.children) == 0:
        return 0
    else:
        total = 0
        for c in bag.children:
            c_parts = c.split(' ')
            mult = int(c_parts[0].strip())
            id = c_parts[1] + ' ' + c_parts[2]
            total += mult + (mult * get_bag_total(id))
        return total


def part2():
    return get_bag_total('shiny gold')

# print("Part 1: " + str(part1()))
print("Part 2: " + str(part2()))
