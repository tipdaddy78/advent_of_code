from itertools import permutations
from util.FileHelper import read_file_multiple_lines

people = set()
relationships = dict()

lines = read_file_multiple_lines('2015', 'day13')

# Data Converstion
for line in lines:
    (p1, _, gainLose, units, _, _, _, _, _, _, p2) = line.strip().split(' ')
    happiness = int(units) * -1 if gainLose == 'lose' else int(units)
    p2 = p2[:-1]
    people.add(p1)
    people.add(p2)
    relationships.setdefault(p1, dict())[p2] = happiness

best = 0
for items in permutations(people):
    happy = sum(map(lambda x, y: relationships[x][y] + relationships[y][x], items, (items[1:]) + (items[0],)))
    best = max(best, happy)

print(best)

# Part 2
for p in people:
    relationships.setdefault(p, dict())['me'] = 0
    relationships.setdefault('me', dict())[p] = 0

people.add('me')
best = 0
for items in permutations(people):
    happy = sum(map(lambda x, y: relationships[x][y] + relationships[y][x], items, (items[1:]) + (items[0],)))
    best = max(best, happy)

print(best)