puzzle_input = list()
with open('day1.txt', 'r') as f:
    puzzle_input = f.readlines()
    f.close()

def part1():
    for i in range(0, len(puzzle_input)):
        for j in range(i+1, len(puzzle_input)):
            if int(puzzle_input[i]) + int(puzzle_input[j]) == 2020:
                return(int(puzzle_input[i]) * int(puzzle_input[j]))

def part2():
    for i in range(0, len(puzzle_input)):
        for j in range(i+1, len(puzzle_input)):
            for k in range(j+1, len(puzzle_input)):
                if (int(puzzle_input[i]) + int(puzzle_input[j]) + int(puzzle_input[k])) == 2020:
                    return(int(puzzle_input[i]) * int(puzzle_input[j]) * int(puzzle_input[k]))

print(part1())
print(part2())