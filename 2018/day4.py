lines = list()
with open('day4.txt', 'r') as f:
    lines = f.readlines()
    f.close()

part1 = False
guard_dict = dict()
cur_row = -1
lines.sort()
cur_min = 0
cur_ID = cur_id = lines[0].split(' ')[3]
awake = True

for line in lines:
    dateString = line[1:17]
    date_parts = dateString.split(' ')
    minute = int(date_parts[1].split(":")[1])
    if line[19] == "G":
        cur_row += 1
        cur_ID = line.split(' ')[3]
        time_dict =  guard_dict.get(cur_ID)
        if time_dict == None:
            time_dict = dict()
            guard_dict[cur_ID] = time_dict
        awake = True
        cur_min = 0
        continue
    else:
        for i in range(cur_min, minute):
            if not awake:
                time = guard_dict.get(cur_ID).get(i)
                if time == None:
                    time = 0
                time += 1
                guard_dict.get(cur_ID)[i] = time
        awake = not awake
        cur_min = minute

sleepiest_id = ''
sleepiest_time = 0
sleepiest_min = 0
if (part1):
    for id in guard_dict.keys():
        sleep_time = 0
        for minute in guard_dict.get(id).keys():
            sleep_time += guard_dict.get(id).get(minute)
        if sleep_time > sleepiest_time:
            sleepiest_time = sleep_time
            sleepiest_id = id

    sleepiest_time = 0
    for minute in guard_dict.get(sleepiest_id).keys():
        if guard_dict.get(sleepiest_id).get(minute) > sleepiest_time:
            sleepiest_time = guard_dict.get(sleepiest_id).get(minute)
            sleepiest_min = minute
else:
    for id in guard_dict.keys():
        for minute in guard_dict.get(id).keys():
            if guard_dict.get(id).get(minute) > sleepiest_time:
                sleepiest_id = id
                sleepiest_time = guard_dict.get(id).get(minute)
                sleepiest_min = minute



print(sleepiest_id)
print(sleepiest_min)