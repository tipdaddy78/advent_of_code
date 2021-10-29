import sys
from itertools import permutations
from util.FileHelper import read_file_multiple_lines

nodes = dict()
distances = dict()
places = set()

lines = read_file_multiple_lines('2015', 'day9.txt')

# Data Conversion
for line in lines:
    parts = line.strip().split('=')
    dist = int(parts[1])
    dests = parts[0].split('to')
    fr = dests[0].strip()
    to = dests[1].strip()
    places.add(fr)
    places.add(to)
    distances.setdefault(fr, dict())[to] = dist
    distances.setdefault(to, dict())[fr] = dist


short = sys.maxsize
long = 0
# Using permutations because each destination connects to each other destination
for items in permutations(places):
    # Below line makes a summation by doing the following
    # x = a list of all but last element
    # y = a list of all but first element
    # finds distance stored for x -> y
    # adds it to the sum
    dist = sum(map(lambda x, y: distances[x][y], items[:-1], items[1:]))
    short = min(short, dist)
    long = max(long, dist)

print("Shortest:", short)
print("Longest:", long)
