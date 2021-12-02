from util.FileHelper import read_file_multiple_lines

depths = read_file_multiple_lines('2021', 'day1')

x = int("123\n")

last = -1
count = 0
for d in depths:
    if last != -1 and last < int(d):
        count += 1
    last = int(d)

# Part 2
last = -1
pt2_count = 0
for i in range(len(depths) - 2):
    cur = int(depths[i]) + int(depths[i+1]) + int(depths[i+2])
    if last != -1 and last < cur:
        pt2_count += 1
    last = cur

print(count)
print(pt2_count)
