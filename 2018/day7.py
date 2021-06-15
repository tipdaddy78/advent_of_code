inst = list()
with open('day7.txt', 'r') as f:
    inst = f.readlines()
    f.close()

c_dict = dict()
tasks = dict()

for i in inst:
    p = i.strip().split(' ')
    cur_c = c_dict.get(p[1])
    if cur_c == None:
        cur_c = set()
    cur_c.add(p[7])
    c_dict[p[1]] = cur_c
    tasks[p[1]] = ord(p[1]) - 5
    tasks[p[7]] = ord(p[7]) - 5

workers_task = ['','', '', '', '']
workers_time = [0, 0, 0, 0, 0]
total = len(tasks)
available = set()
completed = ''
root = ''
for t in tasks:
    child = False
    for c_list in c_dict.values():
        if not child:
            if t in c_list:
                child = True
    if not child:
        available.add(t)

time = -1
while len(completed) != total:
    time += 1
    for i in range(len(workers_task)):
        if workers_time[i] > 0:
            workers_time[i] -= 1
            continue
        if (workers_task[i] != ''):
            completed += workers_task[i]
        comp = workers_task[i]
        if comp in c_dict.keys():
            to_add = list()
            for c in c_dict.get(comp):
                ready = True
                for a in c_dict.keys():
                    if ready and a != comp and a not in completed and c in c_dict.get(a):
                        ready = False
                        break
                if ready:
                    to_add.append(c)
            for t in to_add:
                available.add(t)

        to_do = ''
        if (len(available) > 0):
            to_do = min(available)
            available.remove(to_do)
        workers_task[i] = to_do
        if to_do != '':
            workers_time[i] = (tasks.get(to_do))

        if comp in c_dict.keys():
            c_dict.pop(comp)


print(time)





