import sys
from collections import Counter
from util.FileHelper import read_file_multiple_lines

data = read_file_multiple_lines('2021', 'day14')
polymer = data[0].strip()
insertion_rules = dict()
pairs = dict()
letter_counts = Counter(polymer)

for i in range(2, len(data)):
    line_parts = data[i].strip().split(' -> ')
    insertion_rules[line_parts[0]] = line_parts[1]
for i in range(len(polymer)-1):
    cur_pair = polymer[i] + polymer[i+1]
    pairs[cur_pair] = pairs.get(cur_pair, 0) + 1

# Part 2 = 40 steps
for n in range(40):
    new_pairs = dict()
    for k, v in pairs.items():
        insert = insertion_rules.get(k)
        if insert:
            new_pairs[k[0] + insert] = new_pairs.get(k[0] + insert, 0) + v
            new_pairs[insert + k[1]] = new_pairs.get(insert + k[1], 0) + v
            letter_counts[insert] = letter_counts.get(insert, 0) + v
    pairs = new_pairs

max_letter = 0
min_letter = sys.maxsize
for v in letter_counts.values():
    max_letter = max(v, max_letter)
    min_letter = min(v, min_letter)

print(max_letter - min_letter)
