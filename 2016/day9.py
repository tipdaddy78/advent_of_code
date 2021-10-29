from util.FileHelper import read_file_single_line

directions = read_file_single_line('2016', 'day9')
# directions = "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"


def decompress(d, v2=False):
    res = ''
    i = 0
    while i < len(d.strip()):
        if d[i] != '(':
            if d[i] == ' ':
                i += 1
                continue
            res += d[i]
            i += 1
        else:
            endOfMarker = d.find(')', i)
            marker = d[i + 1:endOfMarker].strip().split('x')
            charsToGet = int(marker[0])
            repetitions = int(marker[1])
            i = endOfMarker + 1
            if v2:
                repetition = decompress(d[i:i + charsToGet], True)
            else:
                repetition = d[i:i + charsToGet]
            for n in range(repetitions):
                res += repetition
            i += charsToGet
    return res


# part1 = decompress(directions)
# print(len(part1))
part2 = decompress(directions, True)
# print(part2)
print(len(part2))
