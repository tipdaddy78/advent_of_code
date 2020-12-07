puzzle_input = list()
with open('day5.txt', 'r') as f:
    puzzle_input = f.readlines()
    f.close()

def process(part2):
    filled_seats = list()
    max = 0
    for p in puzzle_input:
        row_in = p[:7].strip()
        col_in = p[7:].strip()
        r_binary = ''
        for r in row_in:
            if r == 'F':
                r_binary += '0'
            else:
                r_binary += '1'
        row = int(r_binary, 2)
        c_binary = ''
        for c in col_in:
            if c == 'R':
                c_binary += '1'
            else:
                c_binary += '0'
        col = int(c_binary, 2)
        seat_id = row * 8 + col
        if part2:
            filled_seats.append(str(row) + "-" + str(col))
        if seat_id > max:
            max = seat_id
    if part2:
        seats = list()
        for r in range(5, 128):
            for c in range(8):
                seat = str(r) + '-' + str(c)
                if seat not in filled_seats:
                    seats.append(seat)
        return str(int(seats[0].split('-')[0]) * 8 + int(seats[0].split('-')[1]))
    else:
        return max







print("Part 1: "  + str(process(False)))
print("Part 2: "  + str(process(True)))