from math import gcd

with open('day12.txt', 'r') as f:
    data = f.readlines()
    f.close()

test_moons = [
'<x=-1, y=0, z=2>',
'<x=2, y=-10, z=-7>',
'<x=4, y=-8, z=8>',
'<x=3, y=5, z=-1>'
]

test_moons2 = [
'<x=-8, y=-10, z=0>',
'<x=5, y=5, z=10>',
'<x=2, y=-7, z=3>',
'<x=9, y=-8, z=-3>',
]


class moon:
    def __init__(self, id, x, y, z):
        self.id = id
        self.x = x
        self.y = y
        self.z = z
        self.x_vel = 0
        self.y_vel = 0
        self.z_vel = 0

    def apply_gravity(self, moon2):
        if moon2.id == self.id:
            return
        else:
            if self.x < moon2.x:
                self.x_vel += 1
            elif self.x > moon2.x:
                self.x_vel -= 1
            if self.y < moon2.y:
                self.y_vel += 1
            elif self.y > moon2.y:
                self.y_vel -= 1
            if self.z < moon2.z:
                self.z_vel += 1
            elif self.z > moon2.z:
                self.z_vel -= 1

    def apply_velocity(self):
        self.x += self.x_vel
        self.y += self.y_vel
        self.z += self.z_vel

    def get_total_energy(self):
        pot = abs(self.x) + abs(self.y) + abs(self.z)
        kin = abs(self.x_vel) + abs(self.y_vel) + abs(self.z_vel)
        return (pot * kin)

moons = list()
part1 = False
# data = test_moons2
for i in range(len(data)):
    d = data[i].strip().replace('<', '').replace('>', '')
    coords = d.split(',')
    m = moon(i, int(coords[0].strip().split('=')[1]), int(coords[1].strip().split('=')[1]), int(coords[2].strip().split('=')[1]))
    moons.append(m)
if part1:
    for i in range(1000):
        for m1 in moons:
            for m2 in moons:
                m1.apply_gravity(m2)
        for m in moons:
            m.apply_velocity()

    total_energy = 0
    for m in moons:
        total_energy += m.get_total_energy()

    print(total_energy)
else:
    x_poss = list()
    x_vels = list()
    y_poss = list()
    y_vels = list()
    z_poss = list()
    z_vels = list()
    for m in moons:
        x_poss.append(m.x)
        x_vels.append(m.x_vel)
        y_poss.append(m.y)
        y_vels.append(m.y_vel)
        z_poss.append(m.z)
        z_vels.append(m.z_vel)
    initial_x = x_poss.copy()
    initial_y = y_poss.copy()
    initial_z = z_poss.copy()

    simulating = True
    x_steps = 0
    y_steps = 0
    z_steps = 0
    while simulating:
        x_steps += 1
        for i in range(len(x_poss)):
            for j in range(len(x_poss)):
                if i == j:
                    continue
                if x_poss[i] < x_poss[j]:
                    x_vels[i] += 1
                elif x_poss[i] > x_poss[j]:
                    x_vels[i] -= 1
        for i in range(len(x_poss)):
            x_poss[i] += x_vels[i]
        if x_poss == initial_x and x_vels == [0, 0, 0, 0]:
            simulating = False
    print(x_steps)

    simulating = True
    while simulating:
        y_steps += 1
        for i in range(len(y_poss)):
            for j in range(len(y_poss)):
                if i == j:
                    continue
                if y_poss[i] < y_poss[j]:
                    y_vels[i] += 1
                elif y_poss[i] > y_poss[j]:
                    y_vels[i] -= 1
        for i in range(len(y_poss)):
            y_poss[i] += y_vels[i]
        if y_poss == initial_y and y_vels == [0, 0, 0, 0]:
            simulating = False
    print(y_steps)

    simulating = True
    while simulating:
        z_steps += 1
        for i in range(len(z_poss)):
            for j in range(len(z_poss)):
                if i == j:
                    continue
                if z_poss[i] < z_poss[j]:
                    z_vels[i] += 1
                elif z_poss[i] > z_poss[j]:
                    z_vels[i] -= 1
        for i in range(len(z_poss)):
            z_poss[i] += z_vels[i]
        if z_poss == initial_z and z_vels == [0, 0, 0, 0]:
            simulating = False
    print(z_steps)
