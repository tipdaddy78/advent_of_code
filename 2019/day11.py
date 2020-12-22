if __name__ == "__main__": # Local Run
    import intcode_computer
else: # Module Run, When going production - delete if/else
    from . import intcode_computer

puzzle_input = list()
with open('day11.txt', 'r') as f:
    puzzle_input = f.readline().split(',')
    f.close()

class PaintingRobot:
    def __init__(self, instructions):
        self.brain = intcode_computer.Intcode(instructions)

