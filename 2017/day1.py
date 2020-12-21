data = ""
total = 0
with open('day1.txt', 'r') as f:
    data = f.read()
    f.close()

half = int(len(data) / 2)
for i in range(len(data)):
    cur = ""
    next = ""
    if (i + half >= len(data) - 1):
        j = i + half - (len(data) - 1)
        cur = data[i]
        next = data[j]
    else:
        cur = data[i]
        next = data[i+half]

    if cur == next:
        total += int(cur)

print(total)