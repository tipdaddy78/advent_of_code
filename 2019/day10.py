import math

def sortSlope(val):
    if val[0] != 0:
        return abs(val[1]) / abs(val[0])
    else:
        return 1000000000000

with open('day10.txt', 'r') as f:
    grid = f.readlines()
    f.close()

asteroids = dict()
for y in range(len(grid)):
    row = grid[y]
    for x in range(len(row)):
        if row[x] == '#':
            asteroids[(x, y)] = 0

max = 0
max_a = None
part1 = False

if part1:
    for a1 in asteroids.keys():
        count = 0
        for a2 in asteroids.keys():
            if a1 == a2: #Dont need to compute if an asteroid can see itself.
                continue
            x_diff = a2[0] - a1[0]
            y_diff = a2[1] - a1[1]
            gcd = math.gcd(x_diff, y_diff)
            slope_x = x_diff
            slope_y = y_diff
            if gcd != 1:
                slope_x = int(slope_x / gcd)
                slope_y = int(slope_y / gcd)
            cur = a1
            while cur != a2:
                new_cur = (cur[0] + slope_x, cur[1] + slope_y)
                cur = new_cur
                if cur in asteroids.keys() and cur != a2:
                    #another asteroid is blocking the one we want.
                    break
                elif cur in asteroids.keys() and cur == a2:
                    #made it to the asteroid unblocked
                    count += 1
        if count > max:
            max = count
            max_a = a1
    print(max)
    print(max_a)
else:
    slope_dict = dict()
    slope_list_q1 = list()
    slope_list_q2 = list()
    slope_list_q3 = list()
    slope_list_q4 = list()
    base = (25, 31)
    for a in asteroids.keys():
        if a == base:  # Dont need to compute if an asteroid can see itself.
            continue
        x_diff = a[0] - base[0]
        y_diff = a[1] - base[1]
        gcd = math.gcd(x_diff, y_diff)
        slope_x = x_diff
        slope_y = y_diff
        if gcd != 1:
            slope_x = int(slope_x / gcd)
            slope_y = int(slope_y / gcd)
        slope = (slope_x, slope_y)
        if slope in slope_dict.keys():
            slope_list = slope_dict.get(slope).copy()
            slope_list.append(a)
            slope_list.sort()
            slope_dict[slope] = slope_list
        else:
            slope_list = list()
            slope_list.append(a)
            slope_dict[slope] = slope_list
            if (slope[0] > 0 and slope[1] < 0) or  (slope[0] > 0 and slope[1] == 0) or (slope[0] == 0 and slope[1] < 0):
                slope_list_q1.append(slope)
            elif (slope[0] > 0 and slope[1] > 0) or (slope[0] == 0 and slope[1] > 0):
                slope_list_q2.append(slope)
            elif (slope[0] < 0 and slope[1] > 0) or (slope[0] < 0 and slope[1] == 0):
                slope_list_q3.append(slope)
            else:
                slope_list_q4.append(slope)
    slope_list_q1.sort(key = sortSlope, reverse = True)
    slope_list_q2.sort(key = sortSlope)
    slope_list_q3.sort(key = sortSlope, reverse = True)
    slope_list_q4.sort(key = sortSlope)
    combined_slope_list = list()
    combined_slope_list.extend(slope_list_q1)
    combined_slope_list.extend(slope_list_q2)
    combined_slope_list.extend(slope_list_q3)
    combined_slope_list.extend(slope_list_q4)
    idx = 0
    destroyed = list()
    while(len(destroyed) < 200):
        cur_slope = combined_slope_list[idx]
        cur_points = slope_dict.get(cur_slope)
        destroyed.append(cur_points[0])
        cur_points.pop(0)
        if len(cur_points) == 0:
            slope_dict.pop(cur_slope)
            combined_slope_list.pop(idx)
            idx -= 1
        slope_dict[cur_slope] = cur_points
        idx = (idx + 1) % len(combined_slope_list)

    print(destroyed[199])


