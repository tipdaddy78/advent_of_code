if __name__ == "__main__": # Local Run
    import intcode_computer
else: # Module Run, When going production - delete if/else
    from . import intcode_computer

puzzle_input = list()
with open('day2.txt', 'r') as f:
    puzzle_input = f.readline().split(',')
    f.close()


# intcodes = [1,9,10,3,2,3,11,0,99,30,40,50]


def part1():
    intcodes = intcode_computer.Intcode(puzzle_input)
    intcodes.memory[1] = 12
    intcodes.memory[2] = 2
    return intcodes.process()

def part2():
    for n in range(0, 99):
        for v in range(0, 99):
            curr = intcode_computer.Intcode(puzzle_input)
            curr.memory[1] = n
            curr.memory[2] = v
            output = curr.process()
            if (output == 19690720):
                return((100 * n) + v)

print("Part 1: " + str(part1()))
print("Part 2: " + str(part2()))