class Intcode:
    def __init__(self, string_memory, isAI=False):
        self.memory = dict()
        self.pos = 0
        self.base = 0
        self.isAI = isAI
        for i in range(0, len(string_memory)):
            self.memory[i] = int(string_memory[i])
            # self.memory.append(int(s))

    def get_mem_value(self, index):
        if index not in self.memory.keys():
            return 0
        else:
            return self.memory[index]

    def process(self):
        op_code = 0
        modes = list()
        while self.memory[self.pos] != 99:
            op_code = self.memory[self.pos]
            modes = list()
            if (op_code > 99):
                t_op = str(op_code)[-2:]
                t_modes = str(op_code)[:-2]
                op_code = int(t_op)
                modes = t_modes[::-1]
            if (op_code == 1):
                self.op_1(self.memory[self.pos + 1],
                          self.memory[self.pos + 2],
                          self.memory[self.pos + 3],
                          int(modes[0]) if len(modes) >= 1 else 0,
                          int(modes[1]) if len(modes) >= 2 else 0,
                          int(modes[2]) if len(modes) >= 3 else 0)
            elif (op_code == 2):
                self.op_2(self.memory[self.pos + 1],
                          self.memory[self.pos + 2],
                          self.memory[self.pos + 3],
                          int(modes[0]) if len(modes) >= 1 else 0,
                          int(modes[1]) if len(modes) >= 2 else 0,
                          int(modes[2]) if len(modes) >= 3 else 0)
            elif (op_code == 3):
                self.op_3(self.memory[self.pos + 1],
                          int(modes[0]) if len(modes) >= 1 else 0)
            elif (op_code == 4):
                self.op_4(self.memory[self.pos + 1],
                          int(modes[0]) if len(modes) >= 1 else 0)
            elif (op_code == 5):
                self.op_5(self.memory[self.pos + 1],
                          self.memory[self.pos + 2],
                          int(modes[0]) if len(modes) >= 1 else 0,
                          int(modes[1]) if len(modes) >= 2 else 0)
            elif (op_code == 6):
                self.op_6(self.memory[self.pos + 1],
                          self.memory[self.pos + 2],
                          int(modes[0]) if len(modes) >= 1 else 0,
                          int(modes[1]) if len(modes) >= 2 else 0)
            elif op_code == 7:
                self.op_7(self.memory[self.pos + 1],
                          self.memory[self.pos + 2],
                          self.memory[self.pos + 3],
                          int(modes[0]) if len(modes) >= 1 else 0,
                          int(modes[1]) if len(modes) >= 2 else 0,
                          int(modes[2]) if len(modes) >= 3 else 0)
            elif op_code == 8:
                self.op_8(self.memory[self.pos + 1],
                          self.memory[self.pos + 2],
                          self.memory[self.pos + 3],
                          int(modes[0]) if len(modes) >= 1 else 0,
                          int(modes[1]) if len(modes) >= 2 else 0,
                          int(modes[2]) if len(modes) >= 3 else 0)
            elif (op_code == 9):
                self.op_9(self.memory[self.pos + 1],
                          int(modes[0]) if len(modes) >= 1 else 0)

        return self.memory[0]


    def op_1(self, p1, p2, p3, m1, m2, m3):
        add1 = 0
        add2 = 0
        if m1 == 1:
            add1 = p1
        elif m1 == 2:
            add1 = self.get_mem_value(self.base + p1)
        else:
            add1 = self.get_mem_value(p1)

        if m2 == 1:
            add2 = p2
        elif m2 == 2:
            add2 = self.get_mem_value(self.base + p2)
        else:
            add2 = self.get_mem_value(p2)

        if m3 == 2:
            self.memory[self.base + p3] = add1 + add2
        else:
            self.memory[p3] = add1 + add2
        self.pos += 4

    def op_2(self, p1, p2, p3, m1, m2, m3):
        mult1 = 0
        mult2 = 0
        if m1 == 1:
            mult1 = p1
        elif m1 == 2:
            mult1 = self.get_mem_value(self.base + p1)
        else:
            mult1 = self.get_mem_value(p1)

        if m2 == 1:
            mult2 = p2
        elif m2 == 2:
            mult2 = self.get_mem_value(self.base + p2)
        else:
            mult2 = self.get_mem_value(p2)

        if m3 == 2:
            self.memory[self.base + p3] = mult1 * mult2
        else:
            self.memory[p3] = mult1 * mult2
        self.pos += 4

    def op_3_human(self, p1, m1):
        i = input("Please enter an input parameter: ")
        if m1 == 2:
            self.memory[self.base + p1] = int(i)
        else:
            self.memory[p1] = int(i)
        self.pos += 2

    def op_4(self, p1, m1):
        if m1 == 1:
            print(p1)
        elif m1 == 2:
            print(self.get_mem_value(self.base + p1))
        else:
            print(self.get_mem_value(p1))
        self.pos += 2

    def op_5(self, p1, p2, m1, m2):
        op1 = 0
        op2 = 0
        if m1 == 1:
            op1 = p1
        elif m1 == 2:
            op1 = self.get_mem_value(self.base + p1)
        else:
            op1 = self.get_mem_value(p1)

        if m2 == 1:
            op2 = p2
        elif m2 == 2:
            op2 = self.get_mem_value(self.base + p2)
        else:
            op2 = self.get_mem_value(p2)

        if op1 != 0:
            self.pos = op2
        else:
            self.pos += 3

    def op_6(self, p1, p2, m1, m2):
        op1 = 0
        op2 = 0
        if m1 == 1:
            op1 = p1
        elif m1 == 2:
            op1 = self.get_mem_value(self.base + p1)
        else:
            op1 = self.get_mem_value(p1)

        if m2 == 1:
            op2 = p2
        elif m2 == 2:
            op2 = self.get_mem_value(self.base + p2)
        else:
            op2 = self.get_mem_value(p2)

        if op1 == 0:
            self.pos = op2
        else:
            self.pos += 3

    def op_7(self, p1, p2, p3, m1, m2, m3):
        op1 = 0
        op2 = 0
        if m1 == 1:
            op1 = p1
        elif m1 == 2:
            op1 = self.get_mem_value(self.base + p1)
        else:
            op1 = self.get_mem_value(p1)

        if m2 == 1:
            op2 = p2
        elif m2 == 2:
            op2 = self.get_mem_value(self.base + p2)
        else:
            op2 = self.get_mem_value(p2)

        if op1 < op2:
            if m3 == 2:
                self.memory[self.base + p3] = 1
            else:
                self.memory[p3] = 1
        else:
            if m3 == 2:
                self.memory[self.base + p3] = 0
            else:
                self.memory[p3] = 0
        self.pos += 4

    def op_8(self, p1, p2, p3, m1, m2, m3):
        op1 = 0
        op2 = 0
        if m1 == 1:
            op1 = p1
        elif m1 == 2:
            op1 = self.get_mem_value(self.base + p1)
        else:
            op1 = self.get_mem_value(p1)

        if m2 == 1:
            op2 = p2
        elif m2 == 2:
            op2 = self.get_mem_value(self.base + p2)
        else:
            op2 = self.get_mem_value(p2)

        if op1 == op2:
            if m3 == 2:
                self.memory[self.base + p3] = 1
            else:
                self.memory[p3] = 1
        else:
            if m3 == 2:
                self.memory[self.base + p3] = 0
            else:
                self.memory[p3] = 0
        self.pos += 4

    def op_9(self, p1, m1):
        op = 0
        if m1 == 1:
            op = p1
        elif m1 == 2:
            op = self.get_mem_value(self.base + p1)
        else:
            op = self.get_mem_value(p1)

        self.base += op
        self.pos += 2