instructions = list()
with open('day8.txt', 'r') as f:
    instructions = f.readlines()
    f.close()

class Handheld:
    def __init__(self, instructions):
        self.instructions = instructions
        self.cmd_set = set()
        self.acc = 0

    def reset(self):
        self.acc = 0
        self.cmd_set = set()

    def process(self, fillJump=True, fillNop=True, jmp_skip=None):
        i = 0
        ins_set = set()
        while i < len(self.instructions):
            cur = self.instructions[i].strip()
            if i in ins_set:
                print("Infinite Loop Detected")
                return False
            else:
                ins_set.add(i)
            if 'nop' in cur:
                if fillNop:
                    self.cmd_set.add(i)
                i += 1
            elif 'acc' in cur:
                self.acc += int(cur.split(' ')[1])
                i += 1
            elif 'jmp' in cur:
                if fillJump:
                    self.cmd_set.add(i)
                if jmp_skip is not None and jmp_skip == i:
                    i += 1
                else:
                    i += int(cur.split(' ')[1])
        return True


def part1():
    hh = Handheld(instructions)
    hh.process()
    return hh.acc

def part2():
    hh = Handheld(instructions)
    hh.process(True, False)
    jmp_set = hh.cmd_set
    hh.reset()
    hh.process(False)
    nop_set = hh.cmd_set
    for j in jmp_set:
        hh.reset()
        if hh.process(False, False, j):
            return hh.acc
    for n in nop_set:
        hh.reset()
        if hh.process(False, False, n):
            return hh.acc

    return -1

print(part1())
print(part2())
