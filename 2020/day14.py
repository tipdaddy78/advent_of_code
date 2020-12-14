puzzle_input = list()
with open('day14.txt', 'r') as f:
    for l in f.readlines():
        puzzle_input.append(l.strip())
    f.close()

class Masker:
    def __init__(self, v):
        self.mask = ''
        self.mem = dict()
        self.instructions = list()
        self.v = v

    def set_mask(self, mask):
        self.mask = mask

    def set_instructions(self, instructions):
        self.instructions = instructions

    def fill_mem(self, dest, dec):
        if self.v == 1:
            b_temp = bin(dec).replace("0b", "").rjust(36, '0')
            b = ''
            for i in range(len(self.mask)):
                if self.v == 1:
                    if self.mask[i] == 'X':
                        b += b_temp[i]
                    else:
                        b += self.mask[i]
                elif self.v == 2:
                    if self.mask[i] == '0':
                        b += b_temp[i]
                    else:
                        b += self.mask[i]
            self.mem[dest] = b
        elif self.v == 2:
            b_temp = bin(dest).replace("0b", "").rjust(36, '0')
            for n in range(pow(2, self.mask.count('X'))):
                b = bin(n).replace("0b", "").rjust(self.mask.count('X'), '0')
                x = 0
                v = ''
                for j in range(len(self.mask)):
                    if self.mask[j] == 'X':
                        if x < len(b):
                            v += b[x]
                        else:
                            v += '0'
                        x += 1
                    elif self.mask[j] == '0':
                        v += b_temp[j]
                    else:
                        v += '1'
                d = int(v, 2)
                self.mem[d] = dec

    def process(self):
        for i in self.instructions:
            p = i.split('=')
            if p[0].strip() == 'mask':
                self.set_mask(p[1].strip())
            else:
                self.fill_mem(int(p[0].strip()[4:-1]), int(p[1].strip()))

        sum = 0
        for k in self.mem.keys():
            if self.v == 1:
                sum += int(self.mem[k], 2)
            elif self.v == 2:
                sum += self.mem[k]
        return sum

def part1():
    m = Masker(1)
    m.set_instructions(puzzle_input)
    return m.process()

def part2():
    m = Masker(2)
    m.set_instructions(puzzle_input)
    return m.process()

# print(part1())
print(part2())