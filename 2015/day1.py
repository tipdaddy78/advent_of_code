from util.FileHelper import read_file_single_line

puzzle = read_file_single_line('2015', 'day1')

floor = 0
first = True
for p in range(len(puzzle)):
    if puzzle[p] == '(':
        floor += 1
    elif puzzle[p] == ')':
        floor -= 1
    if floor < 0 and first:
        first = False
        print("Entering basement as position: " + str(p+1))

print(floor)
