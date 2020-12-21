class state:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.next = None
        self.previous = None
        self.action = None

    def setNext(self, state):
        self.next = state

    def setAction(self, action):
        self.action = action

    def setPrevious(self, state):
        self.previous = state

def find_addr(s1, ac, s2):
    return s1[ac[1]] + s1[ac[2]] == s2[ac[3]]

def find_addi(s1, ac, s2):
    return s1[ac[1]] + ac[2] == s2[ac[3]]

def find_mulr(s1, ac, s2):
    return s1[ac[1]] * s1[ac[2]] == s2[ac[3]]

def find_muli(s1, ac, s2):
    return s1[ac[1]] * ac[2] == s2[ac[3]]

def find_banr(s1, ac, s2):
    return s1[ac[1]] & s1[ac[2]] == s2[ac[3]]

def find_bani(s1, ac, s2):
    return s1[ac[1]] & ac[2] == s2[ac[3]]

def find_borr(s1, ac, s2):
    return s1[ac[1]] | s1[ac[2]] == s2[ac[3]]

def find_bori(s1, ac, s2):
    return s1[ac[1]] | ac[2] == s2[ac[3]]

def find_setr(s1, ac, s2):
    return s1[ac[1]] == s2[ac[3]]

def find_seti(s1, ac, s2):
    return ac[1] == s2[ac[3]]

def find_gtir(s1, ac, s2):
    return ((ac[1] > s1[ac[2]]) and (s2[ac[3]] == 1)) or ((ac[1] <= s1[ac[2]]) and (s2[ac[3]] == 0))

def find_gtri(s1, ac, s2):
    return ((s1[ac[1]] > ac[2]) and (s2[ac[3]] == 1)) or ((s1[ac[1]] <= ac[2]) and (s2[ac[3]] == 0))

def find_gtrr(s1, ac, s2):
    return ((s1[ac[1]] > s1[ac[2]]) and (s2[ac[3]] == 1)) or ((s1[ac[1]] <= s1[ac[2]]) and (s2[ac[3]] == 0))

def find_eqir(s1, ac, s2):
    return ((ac[1] == s1[ac[2]]) and (s2[ac[3]] == 1)) or ((ac[1] != s1[ac[2]]) and (s2[ac[3]] == 0))

def find_eqri(s1, ac, s2):
    return ((s1[ac[1]] == ac[2]) and (s2[ac[3]] == 1)) or ((s1[ac[1]] != ac[2]) and (s2[ac[3]] == 0))

def find_eqrr(s1, ac, s2):
    return ((s1[ac[1]] == s1[ac[2]]) and (s2[ac[3]] == 1)) or ((s1[ac[1]] != s1[ac[2]]) and (s2[ac[3]] == 0))


def addr(s1, ac):
    s1[ac[3]] = s1[ac[1]] + s1[ac[2]]
    return s1

def addi(s1, ac):
    s1[ac[3]] = s1[ac[1]] + ac[2]
    return s1

def mulr(s1, ac):
    s1[ac[3]] = s1[ac[1]] * s1[ac[2]]
    return s1

def muli(s1, ac):
    s1[ac[3]] = s1[ac[1]] * ac[2]
    return s1

def banr(s1, ac):
    s1[ac[3]] = s1[ac[1]] & s1[ac[2]]
    return s1

def bani(s1, ac):
    s1[ac[3]] =  s1[ac[1]] & ac[2]
    return s1

def borr(s1, ac):
    s1[ac[3]] = s1[ac[1]] | s1[ac[2]]
    return s1

def bori(s1, ac):
    s1[ac[3]] = s1[ac[1]] | ac[2]
    return s1

def setr(s1, ac):
    s1[ac[3]] = s1[ac[1]]
    return s1

def seti(s1, ac):
    s1[ac[3]] = ac[1]
    return s1

def gtir(s1, ac):
    if ac[1] > s1[ac[2]]:
        s1[ac[3]] = 1
    else:
        s1[ac[3]] = 0
    return s1

def gtri(s1, ac):
    if s1[ac[1]] > ac[2]:
        s1[ac[3]] = 1
    else:
        s1[ac[3]] = 0
    return s1

def gtrr(s1, ac):
    if s1[ac[1]] > s1[ac[2]]:
        s1[ac[3]] = 1
    else:
        s1[ac[3]] = 0
    return s1

def eqir(s1, ac):
    if ac[1] == s1[ac[2]]:
        s1[ac[3]] = 1
    else:
        s1[ac[3]] = 0
    return s1

def eqri(s1, ac):
    if s1[ac[1]] == ac[2]:
        s1[ac[3]] = 1
    else:
        s1[ac[3]] = 0
    return s1

def eqrr(s1, ac):
    if s1[ac[1]] == s1[ac[2]]:
        s1[ac[3]] = 1
    else:
        s1[ac[3]] = 0
    return s1

def find_remove_op(opCodes, code, opNum):
    ops = opCodes.get(opNum)
    if code in ops:
        newOps = list()
        for j in range(len(ops)):
            if ops[j] != code:
                newOps.append(ops[j])
        opCodes[opNum] = newOps

lines = list()
with open('day16.txt', 'r') as f:
    lines = f.readlines()
    f.close()

finding_instructions = True
idx = 0
matches3 = 0
allOps = ['addr', 'addi', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori', 'setr', 'seti', 'gtir', 'gtri', 'gtrr', 'eqir', 'eqri', 'eqrr']
opCodes = dict()
for i in range(16):
    opCodes[i] = allOps
while finding_instructions:
    cur = lines[idx]
    matches = 0
    if "Before:" in cur:
        state1 = cur.split(' ')
        a1 = int(state1[1].strip().replace('[', '').replace(',', ''))
        b1 = int(state1[2].strip().replace(',', ''))
        c1 = int(state1[3].strip().replace(',', ''))
        d1 = int(state1[4].strip().replace(']', ''))
        s1 = [a1, b1, c1, d1]
        a = lines[idx+1].split(' ')
        actions = list()
        for ac in a:
            actions.append(int(ac.strip()))
        state2 = lines[idx+2].split(' ')
        a2 = int(state2[2].strip().replace('[', '').replace(',', ''))
        b2 = int(state2[3].strip().replace(',', ''))
        c2 = int(state2[4].strip().replace(',', ''))
        d2 = int(state2[5].strip().replace(']', ''))
        s2 = [a2, b2, c2, d2]

        if find_addr(s1, actions, s2):
            matches += 1
        else:
            find_remove_op(opCodes, 'addr', actions[0])
        if find_addi(s1, actions, s2):
            matches += 1
        else:
            find_remove_op(opCodes, 'addi', actions[0])
        if find_mulr(s1, actions, s2):
            matches += 1
        else:
            find_remove_op(opCodes, 'mulr', actions[0])
        if find_muli(s1, actions, s2):
            matches += 1
        else:
            find_remove_op(opCodes, 'muli', actions[0])
        if find_banr(s1, actions, s2):
            matches += 1
        else:
            find_remove_op(opCodes, 'banr', actions[0])
        if find_bani(s1, actions, s2):
            matches += 1
        else:
            find_remove_op(opCodes, 'bani', actions[0])
        if find_borr(s1, actions, s2):
            matches += 1
        else:
            find_remove_op(opCodes, 'borr', actions[0])
        if find_bori(s1, actions, s2):
            matches += 1
        else:
            find_remove_op(opCodes, 'bori', actions[0])
        if find_setr(s1, actions, s2):
            matches += 1
        else:
            find_remove_op(opCodes, 'setr', actions[0])
        if find_seti(s1, actions, s2):
            matches += 1
        else:
            find_remove_op(opCodes, 'seti', actions[0])
        if find_gtir(s1, actions, s2):
            matches += 1
        else:
            find_remove_op(opCodes, 'gtir', actions[0])
        if find_gtri(s1, actions, s2):
            matches += 1
        else:
            find_remove_op(opCodes, 'gtri', actions[0])
        if find_gtrr(s1, actions, s2):
            matches += 1
        else:
            find_remove_op(opCodes, 'gtrr', actions[0])
        if find_eqir(s1, actions, s2):
            matches += 1
        else:
            find_remove_op(opCodes, 'eqir', actions[0])
        if find_eqri(s1, actions, s2):
            matches += 1
        else:
            find_remove_op(opCodes, 'eqri', actions[0])
        if find_eqrr(s1, actions, s2):
            matches += 1
        else:
            find_remove_op(opCodes, 'eqrr', actions[0])

        if matches >= 3:
            matches3 += 1
        idx += 4
    else:
        finding_instructions = False

identified_instructions = False
finishedOps = set()
while not identified_instructions:
    unfinishedOp = False
    for opCode in opCodes.keys():
        codes = opCodes.get(opCode)
        if len(codes) == 1 and opCode not in finishedOps:
            finishedOps.add(opCode)
            for op2 in opCodes.keys():
                if opCode != op2:
                    find_remove_op(opCodes, codes[0], op2)
        elif len(codes) != 1:
            unfinishedOp = True
    if not unfinishedOp:
        identified_instructions = True
idx += 2
registers = [0, 0, 0, 0]
for i in range(idx, len(lines)):
    a = lines[idx].strip().split()
    action = [int(a[0]), int(a[1]), int(a[2]), int(a[3])]
    code = opCodes.get(action[0])[0]
    if code == 'addr':
        registers = addr(registers, action)
    elif code == 'addi':
        registers = addi(registers, action)
    elif code == 'mulr':
        registers = mulr(registers, action)
    elif code == 'muli':
        registers = muli(registers, action)
    elif code == 'banr':
        registers = banr(registers, action)
    elif code == 'bani':
        registers = bani(registers, action)
    elif code == 'borr':
        registers = borr(registers, action)
    elif code == 'bori':
        registers = bori(registers, action)
    elif code == 'setr':
        registers = setr(registers, action)
    elif code == 'seti':
        registers = seti(registers, action)
    elif code == 'gtir':
        registers = gtir(registers, action)
    elif code == 'gtri':
        registers = gtri(registers, action)
    elif code == 'gtrr':
        registers = gtrr(registers, action)
    elif code == 'eqir':
        registers = eqir(registers, action)
    elif code == 'eqri':
        registers = eqri(registers, action)
    else:
        registers = eqrr(registers, action)
    idx += 1


print(registers[0])


