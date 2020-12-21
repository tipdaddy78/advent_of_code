data = ""
dataList = list()
banks = list()
states = list()
steps = 0

with open('day6.txt', 'r') as f:
    data = f.read()
    f.close()

dataList = data.split('\t')
for entry in dataList:
    entry.replace('\n', '')
    banks.append(int(entry))

while banks not in states:
    cur = list()
    max = 0
    max_i = 0
    steps += 1
    for i in range(len(banks)):
        cur.append(banks[i])
        if banks[i] > max:
            max = banks[i]
            max_i = i
    if cur not in states:
        states.append(cur)
    else:
        break
    banks[max_i] = 0

    cur_i = max_i
    for j in range(max):
        cur_i += 1
        if cur_i >= len(banks):
            cur_i = 0
        banks[cur_i] += 1

old = 0
for i in range(len(states)):
    if states[i] == banks:
        old = i
        break

print(steps - old)

