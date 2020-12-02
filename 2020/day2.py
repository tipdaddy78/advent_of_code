puzzle_input = list()
with open('day2.txt', 'r') as f:
    puzzle_input = f.readlines()
    f.close()

class Password:
    def __init__(self, pw_string):
        parts = pw_string.split(':')
        self.pw = parts[1].strip()
        policy_parts = parts[0].split(' ')
        self.req_char = policy_parts[1].strip()
        p_range = policy_parts[0].strip().split('-')
        self.min = int(p_range[0].strip())
        self.max = int(p_range[1].strip())


    def is_valid_1(self):
        count = self.pw.count(self.req_char)
        if (count >= self.min) and (count <= self.max):
            return True
        else:
            return False

    def is_valid_2(self):
        low = self.pw[self.min - 1]
        high = self.pw[self.max - 1]
        if ((low == self.req_char) and (high != self.req_char))\
                or ((low != self.req_char) and (high == self.req_char)):
            return True
        else:
            return False

def part1():
    count = 0
    for p in puzzle_input:
        pw = Password(p)
        if pw.is_valid_1():
            count += 1
    return count

def part2():
    count = 0
    for p in puzzle_input:
        pw = Password(p)
        if pw.is_valid_2():
            count += 1
    return count

print(str(part2()))