import itertools

class amplifier:
    def __init__(self, codes, firstInput, position, phase, inputVal):
        self.codes = codes
        self.firstInput = firstInput
        self.position = position
        self.phase = phase
        self.inputVal = inputVal

    def setCodes(self, codes):
        self.codes = codes

    def setFirstInput(self, firstInput):
        self.firstInput = firstInput

    def setPosition(self, position):
        self.position = position

    def setInputVal(self, inputVal):
        self.inputVal = inputVal


intcodes = list()
base_intcodes = list()
with open('input/day7.txt', 'r') as f:
    data = f.read()
    string_codes = data.strip().split(',')
    for code in string_codes:
        base_intcodes.append(int(code))
    f.close()

phase_permus = list(itertools.permutations([0, 1, 2, 3, 4]))
pt2_permus = list(itertools.permutations([5, 6, 7, 8, 9]))
max = 0

test_codes = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]

# for permu in phase_permus:
for permu in pt2_permus:
    inputs = [0, -1, -1, -1, -1]
    j = 0
    amps = list()
    firstAmp = True
    # intcodes = test_codes
    for p in permu:
        amp = amplifier(base_intcodes.copy(), True, 0, p, -1)
        if firstAmp:
            amp.setInputVal(0)
            firstAmp = False
        amps.append(amp)
    #for phase in permu:
    while j < len(permu):
        amp = amps[j]
        firstInput = amp.firstInput
        position = amp.position
        intcodes = amp.codes
        while intcodes[position] != 99:
            op_code = intcodes[position]
            e = 0
            if op_code == 1:
                b = intcodes[position + 1]
                c = intcodes[position + 2]
                d = intcodes[position + 3]
                e = intcodes[b] + intcodes[c]
                intcodes[d] = e
                position += 4
            elif op_code == 2:
                b = intcodes[position + 1]
                c = intcodes[position + 2]
                d = intcodes[position + 3]
                e = intcodes[b] * intcodes[c]
                intcodes[d] = e
                position += 4
            elif op_code == 3:
                b = intcodes[position + 1]
                if firstInput:
                    #intcodes[b] = phase
                    intcodes[b] = permu[j]
                    firstInput = False
                    position += 2
                else:
                    if amp.inputVal != -1:
                        intcodes[b] = amp.inputVal
                        amp.setInputVal(-1)
                        position += 2
                    else:
                        amp.setCodes(intcodes)
                        amp.setPosition(position)
                        amp.setFirstInput(firstInput)
                        amps[j] = amp
                        break
            elif op_code == 4:
                b = intcodes[position + 1]
                cur_input = intcodes[b]
                print(intcodes[b])
                amp2 = amps[((j + 1) % 5)]
                amp2.setInputVal(intcodes[b])
                amps[((j + 1) % 5)] = amp2
                position += 2
            elif op_code == 5:
                b = intcodes[position + 1]
                c = intcodes[position + 2]
                if intcodes[b] != 0:
                    position = intcodes[c]
                else:
                    position += 3
            elif op_code == 6:
                b = intcodes[position + 1]
                c = intcodes[position + 2]
                if intcodes[b] == 0:
                    position = intcodes[c]
                else:
                    position += 3
            elif op_code == 7:
                b = intcodes[position + 1]
                c = intcodes[position + 2]
                d = intcodes[position + 3]
                if intcodes[b] < intcodes[c]:
                    intcodes[d] = 1
                else:
                    intcodes[d] = 0
                position += 4
            elif op_code == 8:
                b = intcodes[position + 1]
                c = intcodes[position + 2]
                d = intcodes[position + 3]
                if intcodes[b] == intcodes[c]:
                    intcodes[d] = 1
                else:
                    intcodes[d] = 0
                position += 4
            else: #Parameter Modes
                str_op = str(op_code)[::-1]
                param_op = int(str_op[0])
                b_mode = True
                c_mode = True
                d_mode = True
                b = intcodes[position + 1]
                c = intcodes[position + 2]
                d = intcodes[position + 3]
                for i in range(2, len(str_op)):
                    if i == 2:
                        if int(str_op[i]) == 1:
                            b_mode = False
                    elif i == 3:
                        if int(str_op[i]) == 1:
                            c_mode = False
                    elif i == 4:
                        if int(str_op[i]) == 1:
                            d_mode = False

                op1 = -1
                op2 = -1
                if b_mode:
                    op1 = intcodes[b]
                else:
                    op1 = b
                if param_op != 3 and param_op != 4:
                    if c_mode:
                        op2 = intcodes[c]
                    else:
                        op2 = c
                if param_op == 1:
                    e = op1 + op2
                    intcodes[d] = e
                    position += 4
                elif param_op == 2:
                    e = op1 * op2
                    intcodes[d] = e
                    position += 4
                elif param_op == 4:
                    cur_input = op1
                    print(op1)
                    amp2 = amps[((j + 1) % 5)]
                    amp2.setInputVal(intcodes[op1])
                    amps[((j + 1) % 5)] = amp2
                    position += 2
                elif param_op == 5:
                    if op1 != 0:
                        position = op2
                    else:
                        position += 3
                elif param_op == 6:
                    if op1 == 0:
                        position = op2
                    else:
                        position += 3
                elif param_op == 7:
                    if op1 < op2:
                        intcodes[d] = 1
                    else:
                        intcodes[d] = 0
                    position += 4
                elif param_op == 8:
                    if op1 == op2:
                        intcodes[d] = 1
                    else:
                        intcodes[d] = 0
                    position += 4
        if intcodes[position] == 99:
            print('ENDED')
            if j == 4:
                break
            # break
        j = (j + 1) % 5
    if cur_input > max:
        max = cur_input
        max_permu = permu

print(max)
print(max_permu)
