puzzle_input = list()
with open('day12.txt', 'r') as f:
    for l in f.readlines():
        puzzle_input.append(l.strip())
    f.close()

class Ship:
    def __init__(self):
        self.dir = 'E'
        self.rot = 90
        self.x = 0
        self.y = 0
        self.w_x = 10
        self.w_y = 1
        self.instructions = list()

    def set_instructions(self, ins):
        self.instructions = ins

    def follow_instructions(self, p):
        for i in self.instructions:
            d = i[0]
            v = int(i[1:])
            if d == 'L' or d == 'R':
                self.rotate(d, v, p)
            elif d == 'F':
                if p == 1:
                    self.move(self.dir, v, p)
                else:
                    self.move(d, v, p)
            else:
                self.move(d, v, p)

    def move(self, d, v, p):
        if p == 1:
            if d == 'N':
                self.y += v
            elif d == 'E':
                self.x += v
            elif d == 'S':
                self.y -= v
            elif d == 'W':
                self.x -= v
        elif p == 2:
            if d == 'N':
                self.w_y += v
            elif d == 'E':
                self.w_x += v
            elif d == 'S':
                self.w_y -= v
            elif d == 'W':
                self.w_x -= v
            elif d == 'F':
                for x in range(v):
                    self.x += self.w_x
                    self.y += self.w_y

    def rotate(self, d, v, p):
        if p == 1:
            if d == 'R':
                self.rot = (self.rot + v) % 360
            elif d == 'L':
                self.rot = (self.rot + (360 - v)) % 360
            if self.rot == 0:
                self.dir = 'N'
            elif self.rot == 90:
                self.dir = 'E'
            elif self.rot == 180:
                self.dir = 'S'
            elif self.rot == 270:
                self.dir = 'W'
        elif p == 2:
            if d == 'L':
                r = 360 - v
            else:
                r = v
            temp_x = self.w_x
            temp_y = self.w_y
            if r == 90:
                self.w_x = temp_y
                self.w_y = temp_x * -1
            elif r == 180:
                self.w_x = temp_x * -1
                self.w_y = temp_y * -1
            elif r == 270:
                self.w_x = temp_y * -1
                self.w_y = temp_x


    def calc_dist(self):
        return abs(self.x) + abs(self.y)


def part1():
    ship = Ship()
    ship.set_instructions(puzzle_input)
    ship.follow_instructions(1)
    return ship.calc_dist()

def part2():
    ship = Ship()
    ship.set_instructions(puzzle_input)
    ship.follow_instructions(2)
    return ship.calc_dist()

print(part1())
print(part2())