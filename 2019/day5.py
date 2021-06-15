intcodes = list()
input_val = 5

with open('day5.txt', 'r') as f:
    data = f.read()
    string_codes = data.strip().split(',')
    for code in string_codes:
        intcodes.append(int(code))
    f.close()

test_intcodes = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

position = 0
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
        intcodes[b] = input_val
        position += 2
    elif op_code == 4:
        b = intcodes[position + 1]
        print(intcodes[b])
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
            print(op1)
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
