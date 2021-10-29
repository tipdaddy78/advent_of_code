from util.FileHelper import read_file_multiple_lines


class Bot:
    def __init__(self, id):
        self.id = id
        self.chips = list()

    def can_give(self):
        return len(self.chips) == 2

    def is_part_1_solution(self):
        if self.can_give():
            return (self.chips[0] == 61 and self.chips[1] == 17) or (self.chips[0] == 17 and self.chips[1] == 61)
        else:
            return False

    def give(self):
        return (self.chips[0], self.chips[1]) if self.chips[0] < self.chips[1] else (self.chips[1], self.chips[0])

    def can_receive(self):
        return len(self.chips) > 2

    def receive(self, chip):
        self.chips.append(chip)


bot_dict = dict()
output = dict()
directions = read_file_multiple_lines('2016', 'day10')


while len(directions) > 0:
    new_directions = list()
    for d in directions:
        parts = d.strip().split(' ')
        # Value assignment
        if d.startswith('value'):
            bot = bot_dict.get(parts[5], Bot(parts[5]))
            bot.receive(int(parts[1]))
            bot_dict[parts[5]] = bot
        else:
            bot = bot_dict.get(parts[1], Bot(parts[1]))
            if not bot.can_give():
                new_directions.append(d)
            else:
                if bot.is_part_1_solution():
                    print("Part 1 solution is bot", bot.id)
                loHi = bot.give()
                # Give low value
                if parts[5] == 'output':
                    output[parts[6]] = loHi[0]
                else:
                    loBot = bot_dict.get(parts[6], Bot(parts[6]))
                    loBot.receive(loHi[0])
                    bot_dict[parts[6]] = loBot
                # Give high value
                if parts[10] == 'output':
                    output[parts[11]] = loHi[1]
                else:
                    hiBot = bot_dict.get(parts[11], Bot(parts[11]))
                    hiBot.receive(loHi[1])
                    bot_dict[parts[11]] = hiBot
    directions = new_directions

print(output['0'] * output['1'] * output['2'])




