def manhattan_distance(x1, y1, x2, y2):
    return(abs(x2 - x1) + abs(y2 - y1))


coordinates = list()
with open('day6.txt', 'r') as f:
    coordinates = f.readlines()
    f.close()

c_dict = dict()
for i in range(len(coordinates)):
    c = coordinates[i].strip().split(',')
    point = (int(c[0]), int(c[1]))
    c_dict[i] = point

