from util.FileHelper import read_file_multiple_lines

directions = read_file_multiple_lines('2015', 'day7')


class CPU:
    def __init__(self):
        self.mem = dict()

    def set_mem_val(self, val, m1):
        if not val.isnumeric():
            if val in self.mem.keys():
                v = int(self.mem[val], 2)
            else:
                return
        else:
            v = int(val)
        self.mem[m1] = bin(v).replace('0b', '').rjust(16, '0')

    def and_op(self, m1, m2, m3):
        if m1.isnumeric():
            op1 = int(m1)
        else:
            if m1 in self.mem.keys():
                op1 = int(self.mem[m1], 2)
            else:
                return
        if m2.isnumeric():
            op2 = int(m2)
        else:
            if m2 in self.mem.keys():
                op2 = int(self.mem[m2], 2)
            else:
                return
        self.mem[m3] = bin(op1 & op2).replace('0b', '').rjust(16, '0')

    def or_op(self, m1, m2, m3):
        if m1.isnumeric():
            op1 = int(m1)
        else:
            if m1 in self.mem.keys():
                op1 = int(self.mem[m1], 2)
            else:
                return
        if m2.isnumeric():
            op2 = int(m2)
        else:
            if m2 in self.mem.keys():
                op2 = int(self.mem[m2], 2)
            else:
                return
        self.mem[m3] = bin(op1 | op2).replace('0b', '').rjust(16, '0')

    def lshift_op(self, m1, v, m2):
        if m1.isnumeric():
            op = bin(int(m1)).replace('0b', '').rjust(16, '0')
        else:
            if m1 in self.mem.keys():
                op = self.mem[m1].replace('0b', '').rjust(16, '0')
            else:
                return
        i = int(op, 2)
        self.mem[m2] = bin(i << v).replace('0b', '').rjust(16, '0')

    def rshift_op(self, m1, v, m2):
        if m1.isnumeric():
            op = bin(int(m1)).replace('0b', '').rjust(16, '0')
        else:
            if m1 in self.mem.keys():
                op = self.mem[m1].replace('0b', '').rjust(16, '0')
            else:
                return
        i = int(op, 2)
        self.mem[m2] = bin(i >> v).replace('0b', '').rjust(16, '0')


    def not_op(self, m1, m2):
        if m1.isnumeric():
            op = bin(int(m1)).replace('0b', '').rjust(16, '0')
        else:
            if m1 in self.mem.keys():
                op = self.mem[m1].replace('0b', '').rjust(16, '0')
            else:
                return
        new = ''
        for o in op:
            if o == '0':
                new += '1'
            else:
                new += '0'
        self.mem[m2] = new

cpu = CPU()
def process():
    read = list()
    while len(read) != len(directions):
        for direction in directions:
            if direction not in read:
                dir_parts = direction.split('->')
                dest = dir_parts[1].strip()
                if dest in cpu.mem.keys():
                    read.append(direction)
                    continue
                if 'AND' in dir_parts[0] or \
                        'OR' in dir_parts[0] or \
                        'LSHIFT' in dir_parts[0] or \
                        'RSHIFT' in dir_parts[0] or \
                        'NOT' in dir_parts[0]:
                    if 'NOT' in dir_parts[0]:
                        cpu.not_op(dir_parts[0].strip().split(' ')[1], dest)
                    else:
                        d = dir_parts[0].strip().split(' ')
                        if 'AND' in dir_parts[0]:
                            cpu.and_op(d[0].strip(), d[2].strip(), dest)
                        elif 'OR' in dir_parts[0]:
                            cpu.or_op(d[0].strip(), d[2].strip(), dest)
                        elif 'LSHIFT' in dir_parts[0]:
                            cpu.lshift_op(d[0].strip(), int(d[2].strip()), dest)
                        elif 'RSHIFT' in dir_parts[0]:
                            cpu.rshift_op(d[0].strip(), int(d[2].strip()), dest)
                else:
                    cpu.set_mem_val(dir_parts[0].strip(), dest)
                if dest in cpu.mem.keys():
                    read.append(direction)

process()
print(int(cpu.mem['a'], 2))
temp = cpu.mem['a']
cpu = CPU()
cpu.mem['b'] = temp
process()
print(int(cpu.mem['a'], 2))
