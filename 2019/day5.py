if __name__ == "__main__": # Local Run
    import intcode_computer
else: # Module Run, When going production - delete if/else
    from . import intcode_computer

puzzle_input = list()
with open('day5.txt', 'r') as f:
    puzzle_input = f.readline().split(',')
    f.close()


# intcodes = intcode_computer.Intcode(puzzle_input)
intcodes = intcode_computer.Intcode([104,1125899906842624,99])

intcodes.process()