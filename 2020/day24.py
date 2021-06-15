class Hextile:
    def __init__(self, id):
        self.neighbors = dict()
        self.black = False
        self.id = id
        (x, y) = id
        self.neighbors['e'] = (x + 1, y)
        self.neighbors['w'] = (x - 1, y)
        self.neighbors['ne'] = (x + 0.5, y + 1)
        self.neighbors['nw'] = (x - 0.5, y + 1)
        self.neighbors['se'] = (x + 0.5, y - 1)
        self.neighbors['sw'] = (x - 0.5, y - 1)

def get_input(test):
    lines = list()
    file = ''
    if test:
        file = 'day24_test.txt'
    else:
        file = 'day24.txt'
    with open(file, 'r') as f:
        lines = [line.strip() for line in f]
        f.close()
    return lines

def follow_instructions(lines):
    ref = (0, 0)
    d = dict()
    ref_h = Hextile(ref)
    d[ref] = ref_h

    for line in lines:
        cur_h = ref_h
        i = 0
        while i < len(line):
            cur = line[i]
            i += 1
            if cur in ['n', 's']:
                cur += line[i]
                i += 1
            dest = cur_h.neighbors[cur]
            if dest in d.keys():
                cur_h = d[dest]
            else:
                # need to create new object
                new_h = Hextile(dest)
                d[dest] = new_h
                cur_h = new_h
        # once at our destination, flip the color
        cur_h.black = not cur_h.black
    return d

def count_black(d):
    count = 0
    for k in d.keys():
        if d[k].black:
            count += 1
    return count

def new_day(x_min, x_max, y_min, y_max, d = dict()):
    new_d = dict()
    for y in range(y_min, y_max+1):
        t_x_min = 0
        t_x_max = 0
        # even row, x is whole
        if y % 2 == 0:
            if not x_min.is_integer():
                t_x_min = int(x_min - 0.5)
            else:
                t_x_min = int(x_min)
            if not x_max.is_integer():
                t_x_max = int(x_max + 0.5)
            else:
                t_x_max = int(x_max)
        # odd row, x is float
        else:
            if not x_min.is_integer():
                t_x_min = int(x_min - 0.5)
            else:
                t_x_min = int(x_min)
            if not x_max.is_integer():
                t_x_max = int(x_max - 0.5)
            else:
                t_x_max = int(x_max)
        for x in range(t_x_min, t_x_max):
            n_x = x
            if y % 2 != 0:
                n_x += 0.5
            key = (n_x, y)
            if key in d.keys():
                hex_tile = d[key]
            else:
                hex_tile = Hextile(key)

            b_count = 0
            for n in hex_tile.neighbors.values():
                if n in d.keys():
                    if d[n].black:
                        b_count += 1
            new_h = Hextile(key)
            if hex_tile.black:
                if b_count == 0 or b_count > 2:
                    new_h.black = False
                else:
                    new_h.black = True
            else:
                if b_count == 2:
                    new_h.black = True
                else:
                    new_h.black = False
            new_d[key] = new_h
    return new_d

def run(p_mode, test):
    x_min = 0.0
    x_max = 0.0
    y_min = 0
    y_max = 0
    input = get_input(test)
    hexes = follow_instructions(input)
    print("Part 1: " + str(count_black(hexes)))
    for k in hexes.keys():
        if k[0] > x_max:
            x_max = k[0]
        if k[0] < x_min:
            x_min = k[0]
        if k[1] > y_max:
            y_max = k[1]
        if k[1] < y_min:
            y_min = k[1]
    for days in range(100):
        hexes = new_day(x_min-1, x_max+1, y_min-1, y_max+1, hexes)
        if p_mode:
            print("Day " + str(days + 1) + ": " + str(count_black(hexes)))
        x_min -= 1
        x_max += 1
        y_min -= 1
        y_max += 1
    print("Part 2: " + str(count_black(hexes)))

run(False, False)