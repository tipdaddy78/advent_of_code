def day2_part1():
    lines = list()
    with open('day2.txt', 'r') as f:
        lines = f.readlines()
        f.close()

    twos = 0
    threes = 0

    for line in lines:
        dub_found = False
        trip_found = False
        dictionary = dict((letter, line.count(letter)) for letter in set(line))
        for key in dictionary:
            if (dictionary.get(key) == 2):
                dub_found = True
            elif (dictionary.get(key) == 3):
                trip_found = True
        if (dub_found):
            twos += 1
        if (trip_found):
            threes += 1

    checksum = twos * threes

    print(checksum)

def day2_part2():
    lines = list()
    id1 = 0
    id2 = 0
    common = ''
    with open('day2.txt', 'r') as f:
        lines = f.readlines()
        f.close()
    for i in range(0, len(lines) - 1):
        for j in range(i+1, len(lines) - 1):
            chars_diff = 0
            if(lines[i][0] != lines[j][0] and lines[i][1] != lines[j][1]): #If this isn't true, more than 1 char is different
                continue
            for k in range(0, len(lines[i]) - 1):
                if (lines[i][k] != lines[j][k]):
                    chars_diff += 1
            if (chars_diff == 1):
                id1 = i
                id2 = j
                break
    print("ID1: " + lines[id1])
    print("ID2: " + lines[id2])
    for i in range(0, len(lines[0]) - 1):
        if (lines[id1][i] == lines[id2][i]):
            common += lines[id1][i]
    print(common)

day2_part2()