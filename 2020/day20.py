class PuzzlePiece:
    def __init__(self, id, data):
        self.id = id
        self.data = data
        self.north = ''
        self.east = ''
        self.west = ''
        self.south = ''
        self.borders = self.get_borders()

    def rotate_right(self):
        temp = list(zip(*self.data[::-1]))
        self.data = temp
        self.borders = self.get_borders()

    def rotate_left(self):
        temp = list(reversed(list(zip(*self.data))))
        self.data = temp
        self.borders = self.get_borders()

    def h_flip(self):
        new_data = list()
        for d in self.data:
            new_data.append(d[::-1])
        self.data = new_data
        self.borders = self.get_borders()

    def v_flip(self):
        new_data = list(reversed(self.data))
        self.data = new_data
        self.borders = self.get_borders()


    def get_borders(self):
        borders = list()
        border = ''
        for c in self.data[0]:
            border += c
        borders.append(border)
        self.north = border
        border = ''
        for c in self.data[-1]:
            border += c
        borders.append(border)
        self.south = border
        border = ''
        border2 = ''
        for r in self.data:
            border += r[0]
            border2 += r[-1]
        borders.append(border)
        borders.append(border2)
        self.east = border2
        self.west = border
        return borders

    def get_edge_count(self, edges):
        count = 0
        for e in edges:
            rev = e[::-1]
            if e in self.borders or rev in self.borders:
                count += 1
        return count

    def print(self):
        for line in self.data:
            l = ''
            for c in line:
                l += c
            print(l)
        print()

def parse_input():
    pieces = dict()
    lines = list()
    with open('day20.txt', 'r') as f:
        lines = [line.strip() for line in f]
        f.close()
    i = 0
    id = ''
    data = list()
    while i < len(lines):
        if 'Tile' in lines[i]:
            id = lines[i].replace(':','').split(' ')[1]
            i += 1
        elif '.' in lines[i] or '#' in lines[i]:
            data = list()
            for j in range(i, i + 10):
                line = lines[j]
                d = list()
                for l in line:
                    d.append(l)
                data.append(d)
            piece = PuzzlePiece(id, data)
            pieces[id] = piece
            i += 10
        else:
            i += 1
    return pieces

def get_edge_borders(pieces=dict()):
    border_counts = dict()
    edges = list()
    for piece in pieces.keys():
        for b in pieces[piece].borders:
            rev = b[::-1]
            if b in border_counts:
                border_counts[b] += 1
            elif rev in border_counts:
                border_counts[rev] += 1
            else:
                border_counts[b] = 1
    for b in border_counts.keys():
        if border_counts[b] == 1:
            edges.append(b)
    print("Total Borders is: " + str(len(border_counts.keys())))
    return edges

def manip_piece_0(piece, edges):
    orienting = True
    while orienting:
        rev_n = piece.north[::-1]
        rev_w = piece.west[::-1]
        if piece.north in edges and piece.west in edges:
            orienting = False



pieces = parse_input()
borders = get_edge_borders(pieces)
total = 1
edges = list()
corners = list()
middle = list()
for p in pieces.keys():
    edges = pieces[p].get_edge_count(borders)
    if edges == 2:
        total *= int(p)
print(total)

