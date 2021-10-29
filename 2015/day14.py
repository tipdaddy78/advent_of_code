from util.FileHelper import read_file_multiple_lines


class Reindeer:
    def __init__(self, name, speed, duration, rest):
        self.name = name
        self.speed = speed
        self.duration = duration
        self.rest = rest
        self.cur_sec = 0
        self.flying_sec = 0
        self.resting_sec = 0
        self.flying = False
        self.dist = 0
        self.points = 0

    def increment_time(self):
        if self.cur_sec == 0:
            self.flying = True
        if self.flying:
            self.dist += self.speed
            self.flying_sec += 1
            if self.flying_sec == self.duration:
                self.flying = False
                self.resting_sec = 0
        else:
            self.resting_sec += 1
            if self.resting_sec == self.rest:
                self.flying = True
                self.flying_sec = 0
        self.cur_sec += 1

    def award_point(self):
        self.points += 1


r_dict = dict()
lines = read_file_multiple_lines('2015', 'day14')
for line in lines:
    (n, _, _, s, _, _, d, _, _, _, _, _, _, r, _) = line.strip().split(' ')
    reindeer = Reindeer(n, int(s), int(d), int(r))
    r_dict[n] = reindeer

for i in range(2503):
    farthest = 0
    for r in r_dict.keys():
        rein = r_dict[r]
        rein.increment_time()
        farthest = max(farthest, rein.dist)
        r_dict[r] = rein
    for r in r_dict.keys():
        rein = r_dict[r]
        if rein.dist == farthest:
            rein.award_point()


most = 0
pts = 0
for r in r_dict.keys():
    most = max(most, r_dict[r].dist)
    pts = max(pts, r_dict[r].points)

print(most)
print(pts)
