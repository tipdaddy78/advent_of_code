puzzle_input = list()
with open('day11.txt', 'r') as f:
    for l in f.readlines():
        puzzle_input.append(l.strip())
    f.close()

class WaitingArea:
    def __init__(self):
        self.state = dict()
        self.prev = dict()
        self.neighbors = dict()
        self.rows = 0
        self.cols = 0

    def fill_seats(self, puzzle, part):
        self.rows = len(puzzle)
        self.cols = len(puzzle[0].strip())
        for y in range(self.rows):
            for x in range(self.cols):
                self.state[(x,y)] = puzzle[y][x]
        # determine set of neighbors for each seat once.
        for y in range(self.rows):
            for x in range(self.cols):
                self.neighbors[(x, y)] = self.get_check_list(x, y, part)

    def apply_rules(self, part):
        next = dict()
        for y in range(self.rows):
            for x in range(self.cols):
                if y == 9 and x == 2:
                    z = 'debugging'
                cur = self.state[(x,y)]
                check_list = self.neighbors[(x,y)]
                occ_count = 0
                for c in check_list:
                    if c in self.state.keys():
                        if self.state[c] == '#':
                            occ_count += 1
                if cur == 'L':
                    if occ_count == 0:
                        next[(x,y)] = '#'
                    else:
                        next[(x,y)] = cur
                elif cur == '#':
                    if part == 1:
                        if occ_count >= 4:
                            next[(x,y)] = 'L'
                        else:
                            next[(x,y)] = '#'
                    elif part == 2:
                        if occ_count >= 5:
                            next[(x,y)] = 'L'
                        else:
                            next[(x,y)] = '#'
                else:
                    next[(x,y)] = cur
        self.prev = self.state
        self.state = next

    def should_stop(self):
        return self.prev == self.state

    def get_seats_occ(self):
        count = 0
        for y in range(self.rows):
            for x in range(self.cols):
                if self.state[(x,y)] == '#':
                    count += 1
        return count

    def print(self):
        for y in range(self.rows):
            cur = ''
            for x in range(self.cols):
                cur += self.state[(x, y)]
            print(cur)

    def get_check_list(self, x, y, part):
        check_list = list()
        if part == 1:
            check_list = [(x, y - 1), (x + 1, y - 1), (x + 1, y), (x + 1, y + 1), (x, y + 1), (x - 1, y + 1),
                          (x - 1, y), (x - 1, y - 1)]
        elif part == 2:
            check_list = list()
            # Begin N seat
            for j in range(y - 1, -1, -1):
                if self.state[(x, j)] != '.':
                    check_list.append((x, j))
                    break
            # end N seat
            # begin NE Seat
            i = x + 1
            j = y - 1
            while True:
                if (i, j) in self.state.keys():
                    if self.state[(i, j)] != '.':
                        check_list.append((i, j))
                        break
                    else:
                        i += 1
                        j -= 1
                else:
                    # Reached bounds
                    break
            # end NE seat
            # begin E seat
            for i in range(x + 1, self.cols):
                if self.state[(i, y)] != '.':
                    check_list.append((i, y))
                    break
            # end E seat
            # begin SE seat
            i = x + 1
            j = y + 1
            while True:
                if (i, j) in self.state.keys():
                    if self.state[(i, j)] != '.':
                        check_list.append((i, j))
                        break
                    else:
                        i += 1
                        j += 1
                else:
                    # Reached bounds
                    break
            # end SE seat
            # begin S seat
            for j in range(y + 1, self.rows):
                if self.state[(x, j)] != '.':
                    check_list.append((x, j))
                    break
            # end S seat
            # begin SW seat
            i = x - 1
            j = y + 1
            while True:
                if (i, j) in self.state.keys():
                    if self.state[(i, j)] != '.':
                        check_list.append((i, j))
                        break
                    else:
                        i -= 1
                        j += 1
                else:
                    # Reached bounds
                    break
            # end SW seat
            # begin W seat
            for i in range(x - 1, -1, -1):
                if self.state[(i, y)] != '.':
                    check_list.append((i, y))
                    break
            # end W seat
            # begin NW seat
            i = x - 1
            j = y - 1
            while True:
                if (i, j) in self.state.keys():
                    if self.state[(i, j)] != '.':
                        check_list.append((i, j))
                        break
                    else:
                        i -= 1
                        j -= 1
                else:
                    # Reached bounds
                    break
        return check_list



def part1():
    wa = WaitingArea()
    wa.fill_seats(puzzle_input, 1)
    while not wa.should_stop():
        wa.apply_rules(1)
    return wa.get_seats_occ()

def part2():
    wa = WaitingArea()
    wa.fill_seats(puzzle_input, 2)
    while not wa.should_stop():
        wa.apply_rules(2)
    return wa.get_seats_occ()

print(part1())
print(part2())
