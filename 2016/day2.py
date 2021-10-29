from util.FileHelper import read_file_multiple_lines


class Keypad:
    def __init__(self):
        self.password = ""
        self.pos = []
        self.keypad = []

    def lock_position(self):
        self.password += str(self.keypad[self.pos[0]][self.pos[1]])

    def get_password(self):
        return self.password


class Part1(Keypad):
    def __init__(self):
        super().__init__()
        self.keypad = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        # Initialize where 5 is on the keypad
        self.pos = [1, 1]

    def add_value(self, y_axis=True):
        if y_axis:
            self.pos[0] = min(2, self.pos[0] + 1)
        else:
            self.pos[1] = min(2, self.pos[1] + 1)

    def subtract_value(self, y_axis=True):
        if y_axis:
            self.pos[0] = max(0, self.pos[0] - 1)
        else:
            self.pos[1] = max(0, self.pos[1] - 1)


class Part2(Keypad):
    def __init__(self):
        super().__init__()
        self.keypad = [
            [' ', ' ', '1', ' ', ' '],
            [' ', '2', '3', '4', ' '],
            ['5', '6', '7', '8', '9'],
            [' ', 'A', 'B', 'C', ' '],
            [' ', ' ', 'D', ' ', ' ']
        ]
        # Initialize where 5 is on the keypad
        self.pos = [2, 0]

    def print_position(self):
        print(self.keypad[self.pos[0]][self.pos[1]])

    def add_value(self, y_axis=True):
        if y_axis:
            new = min(4, self.pos[0] + 1)
            if self.keypad[new][self.pos[1]] != " ":
                self.pos[0] = new
        else:
            new = min(4, self.pos[1] + 1)
            if self.keypad[self.pos[0]][new] != " ":
                self.pos[1] = new

    def subtract_value(self, y_axis=True):
        if y_axis:
            new = max(0, self.pos[0] - 1)
            if self.keypad[new][self.pos[1]] != " ":
                self.pos[0] = new
        else:
            new = max(0, self.pos[1] - 1)
            if self.keypad[self.pos[0]][new] != " ":
                self.pos[1] = new


lines = read_file_multiple_lines("2016", "day2")
p1 = Part1()
p2 = Part2()
for line in lines:
    for i in line.strip():
        match i:
            case 'U':
                p1.subtract_value()
                p2.subtract_value()
            case 'D':
                p1.add_value()
                p2.add_value()
            case 'L':
                p1.subtract_value(False)
                p2.subtract_value(False)
            case 'R':
                p1.add_value(False)
                p2.add_value(False)
    p1.lock_position()
    p2.lock_position()

print(p1.get_password())
print(p2.get_password())
