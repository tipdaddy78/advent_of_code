def run():
    input = '247819356'
    # input = '389125467'
    cups = list()
    for c in input:
        cups.append(int(c))
    cur = cups[0]
    c_idx = 0
    dest = 0
    d_idx = -1
    l = len(cups)
    turns = 100
    max = 9
    for t in range(turns):
        if (t + 1) % 1000 == 0:
            print("Turn " + str(t + 1))
        pick_up = list()
        # grab the next cups
        for i in range(3):
            pick_up.append(cups.pop((c_idx + 1) % l))
            l = len(cups)
            if l <= c_idx:
                c_idx -= 1

        # determine destination
        d_test = cur - 1
        if d_test == 0:
            d_test = max
        while True:
            if d_test in cups:
                for x in range(len(cups)):
                    if cups[x] == d_test:
                        dest = cups[x]
                        d_idx = x
                        break
                break
            else:
                d_test -= 1
                if d_test == 0:
                    d_test = max

        # put cups back in
        for i in range(3):
            cups.insert(d_idx + 1, pick_up.pop(-1))
            if d_idx < c_idx:
                c_idx += 1

        # get variables ready for next pass
        l = len(cups)
        c_idx = (c_idx + 1) % l
        cur = cups[c_idx]

    # find cup 1
    idx = 0
    for x in range(len(cups)):
        if cups[x] == 1:
            idx = x
            break
    ret = ''
    idx = (idx + 1) % l
    for x in range(8):
        ret += str(cups[idx])
        idx = (idx + 1) % l

    return ret

def run_v2():
    input = '247819356'
    # input = '389125467'
    cups_d = dict()
    cups = [int(c) for c in input]
    ext = [x for x in range(10, 1000001)]
    cups += ext

    for i in range(len(cups)):
        if i == len(cups) - 1:
            cups_d[cups[i]] = cups[0]
        else:
            cups_d[cups[i]] = cups[i+1]

    start = int(input[0])
    for i in range(10000000):
        a = cups_d[start]
        b = cups_d[a]
        c = cups_d[b]
        cups_d[start] = cups_d[c]
        dest = start - 1
        if dest in [a, b, c] or dest < 1:
            while dest in [a, b, c] or dest < 1:
                dest -= 1
                if dest < 1:
                    dest = 1000000
        cups_d[c] = cups_d[dest]
        cups_d[dest] = a
        start = cups_d[start]

    op1 = cups_d[1]
    op2 = cups_d[op1]
    return op1 * op2

print(run())
print(run_v2())