from datetime import datetime

puzzle_in = [0,1,5,10,3,12,19]

class MemoryGame:
    def __init__(self, start_nbrs = list()):
        self.idx = 0
        self.mem = dict()
        while self.idx < len(start_nbrs):
            self.mem[start_nbrs[self.idx]] = self.idx + 1
            self.idx += 1
            # print("Turn " + str(self.idx) + ": " + str(start_nbrs[self.idx-1]) + " Starting Number")
        self.last = 0
        self.idx += 1

    def play_game(self, turn):
        # print("Turn " + str(self.idx) + ": " + str(self.last))
        while self.idx < turn:
            cur = self.last
            if cur not in self.mem.keys():
                self.last = 0
            else:
                self.last = (self.idx) - self.mem[cur]
            # print("Turn " + str(self.idx + 1) + ": " + str(self.last))
            self.mem[cur] = self.idx
            self.idx += 1
        return self.last

def part1(mg):
    return mg.play_game(2020)

def part2(mg):
    return mg.play_game(30000000)

mg = MemoryGame(puzzle_in)
print(part1(mg))
print(datetime.now())
print(part2(mg))
print(datetime.now())