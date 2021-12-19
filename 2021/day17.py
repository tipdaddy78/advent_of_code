from util.FileHelper import read_file_single_line, read_file_multiple_lines


class ProbeLauncher:
    def __init__(self, tx_min, tx_max, ty_min, ty_max):
        self.tx_min = tx_min
        self.tx_max = tx_max
        self.ty_min = ty_min
        self.ty_max = ty_max
        self.x = 0
        self.y = 0
        self.vx = 0
        self.vy = 0
        self.max_y = 0

    def shoot(self, vx, vy):
        self.x = 0
        self.y = 0
        self.vx = vx
        self.vy = vy
        self.max_y = 0
        while True:
            self.take_step()
            if self.tx_min <= self.x <= self.tx_max and self.ty_min <= self.y <= self.ty_max:
                return True
            if self.x > self.tx_max or self.y < self.ty_min:
                return False

    def take_step(self):
        self.x += self.vx
        self.y += self.vy
        self.max_y = max(self.y, self.max_y)
        if self.vx > 0:
            self.vx -= 1
        elif self.vx < 0:
            self.vx += 1
        self.vy -= 1


data = read_file_single_line('2021', 'day17')
_, _, x_parts, y_parts = data.strip().split(' ')
x_min, x_max = [int(x.replace(',', '')) for x in x_parts.split('=')[1].split('..')]
y_min, y_max = [int(y.replace(',', '')) for y in y_parts.split('=')[1].split('..')]

launcher = ProbeLauncher(x_min, x_max, y_min, y_max)
hit_maxes = list()
hit_points = set()
for x in range(200):
    for y in range(-176, 250):
        hit = launcher.shoot(x, y)
        if hit:
            hit_maxes.append(launcher.max_y)
            hit_points.add((x, y))

print(max(hit_maxes))
print(len(hit_points))
