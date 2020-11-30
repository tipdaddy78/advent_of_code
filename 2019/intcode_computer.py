class Intcode:
    def __init__(self, string_memory):
        self.memory = list()
        for s in string_memory:
            self.memory.append(int(s))

    def process(self):
        op_code = 0
        pos = 0
        while self.memory[pos] != 99:
            op_code = self.memory[pos]
            if (op_code == 1):
                add1 = self.memory[pos + 1]
                add2 = self.memory[pos + 2]
                dest = self.memory[pos + 3]
                self.memory[dest] = self.memory[add1] + self.memory[add2]
            elif (op_code == 2):
                mult1 = self.memory[pos + 1]
                mult2 = self.memory[pos + 2]
                dest = self.memory[pos + 3]
                self.memory[dest] = self.memory[mult1] * self.memory[mult2]
            pos += 4
        return self.memory[0]