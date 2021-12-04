from util.FileHelper import read_file_multiple_lines


# This class represents a bingo board.
# The board is represented as a dict where the key is the number, and the value is the space (eg: (0,0))
# The marked numbers are a set.
class Board:
    def __init__(self):
        self.board = dict()
        self.marked = set()
        self.last = 0

    def add_to_board(self, val, loc):
        self.board[val] = loc

    def add_to_marked(self, val):
        self.marked.add(val)
        self.last = val

    # To determine if we have a bingo we only need to loop through the marked numbers
    # During this loop we maintain two dictionaries for rows and cols
    # The keys to those dicts are the row/col index
    # The vals to those dicts is the number of marked spots in that row/col
    # A Bingo is defined as 5 in a row/column
    def has_bingo(self):
        rows = dict()
        cols = dict()
        for m in self.marked:
            loc = self.board.get(m)
            if loc is not None:
                rows[loc[0]] = rows.get(loc[0], 0) + 1
                cols[loc[1]] = cols.get(loc[1], 0) + 1
        if 5 in rows.values() or 5 in cols.values():
            return True
        else:
            return False

    # Score is calculated by summing all non-marked rows.
    # Then multiplying by the last called number.
    def get_score(self):
        score = 0
        for b in self.board.keys():
            if b not in self.marked:
                score += b
        score *= self.last
        return score


# Data initialization
data = read_file_multiple_lines('2021', 'day4')
called_values = data.pop(0).split(',')
boards = list()
b = None

new_board = False
r = 0
for d in data:
    if not d.strip():
        new_board = True
        r = 0
        if b is not None:
            boards.append(b)
    else:
        if new_board:
            b = Board()
            new_board = False
        row_values = d.strip().split(' ')
        c = 0
        for v in row_values:
            if v.isnumeric():
                b.add_to_board(int(v), (r, c))
                c += 1
        r += 1
# Add last board to boards
boards.append(b)

# Start calling numbers
# New Boards is for part 2, as we want to stop trying to call for a specific board once it's gotten a bingo
for v in called_values:
    new_boards = list()
    for b in boards:
        b.add_to_marked(int(v))
        winner = b.has_bingo()
        if winner:
            # Part 1 Answer will be the first time this happens.
            # Part 2 Answer will be the last time this happens.
            print("BINGOOOOOO")
            print("Winning Score is:", b.get_score())
        else:
            new_boards.append(b)
    boards = new_boards
