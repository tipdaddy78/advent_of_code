strings = list()
with open('day5.txt', 'r') as f:
    strings = f.readlines()
    f.close()

def part1():
    nice = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    naughty = ['ab', 'cd', 'pq', 'xy']
    bad = False
    last = ''
    for string in strings:
        v_count = 0
        double = False
        bad = False
        last = ''
        for s in string.strip():
            if s in vowels:
                v_count += 1
            if s == last:
                double = True
            if str(last + s) in naughty:
                bad = True
            last = s
        if v_count >= 3 and double and not bad:
            nice += 1
    return(nice)

def part2():
    nice = 0
    for string in strings:
        sandwich = False
        dub_dub = False
        for i in range(len(string.strip())):
            if i >= 2:
                if string[i - 2] == string[i]:
                    sandwich = True
            if i < len(string.strip()) - 2:
                if str(string[i] + string[i+1]) in string[i+2:]:
                    dub_dub = True
        if sandwich and dub_dub:
            nice += 1
    return nice

print(part2())