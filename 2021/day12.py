from util.FileHelper import read_file_multiple_lines
from collections import deque, Counter

data = read_file_multiple_lines('2021', 'day12')
caves = dict()

for line in data:
    ends = line.strip().split('-')
    list1 = caves.get(ends[0], set())
    list1.add(ends[1])
    caves[ends[0]] = list1
    list2 = caves.get(ends[1], set())
    list2.add(ends[0])
    caves[ends[1]] = list2


def list_has_lower_dup(steps):
    counts = Counter(steps)
    for k,v in counts.items():
        if k.islower() and v > 1:
            return True
    return False


# Version allows lower-case caves to only be visited once
def take_step_1(finished, in_progress):
    cur = in_progress.popleft()
    for n in caves[cur[-1]]:
        new_list = cur.copy()
        if n == 'end':
            new_list.append(n)
            finished.append(new_list)
        elif n.isupper() or (n.islower() and n not in cur):
            new_list.append(n)
            in_progress.append(new_list)
    return finished, in_progress


# Version two allows a single lower-case cave be visited twice.
def take_step_2(finished, in_progress):
    cur = in_progress.popleft()
    for n in caves[cur[-1]]:
        new_list = cur.copy()
        if n == 'start':
            continue
        elif n == 'end':
            new_list.append(n)
            finished.append(new_list)
        elif n.isupper():
            new_list.append(n)
            in_progress.append(new_list)
        elif n.islower():
            dup = list_has_lower_dup(cur)
            if not dup or n not in cur:
                new_list.append(n)
                in_progress.append(new_list)
    return finished, in_progress


i_p = deque()
i_p.append(['start'])
f = list()
while len(i_p) > 0:
    # f, i_p = take_step_1(f, i_p)
    f, i_p = take_step_2(f, i_p)

print(len(f))
