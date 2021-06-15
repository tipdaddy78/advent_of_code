intcodes = dict()
input_val = 2

with open('day15.txt', 'r') as f:
    data = f.read()
    string_codes = data.strip().split(',')
    for c in range(len(string_codes)):
        intcodes[c] = int(string_codes[c])
    f.close()

# test_intcodes = [104,1125899906842624,99]
# test_intcodes = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
# intcodes.clear()
# for c in range(len(test_intcodes)):
#      intcodes[c] = int(test_intcodes[c])
# intcodes = test_intcodes

position = 0
relative_base = 0
while intcodes[position] != 99:
    op_code = intcodes[position]
    e = 0
    if (position + 1) in intcodes.keys():
        b = intcodes[position + 1]
    else:
        b = 0
    if (position + 2) in intcodes.keys():
        c = intcodes[position + 2]
    else:
        c = 0
    if (position + 3) in intcodes.keys():
        d = intcodes[position + 3]
    else:
        d = 0
    if op_code == 1:
        if b in intcodes.keys():
            op1 = intcodes[b]
        else:
            op1 = 0
        if c in intcodes.keys():
            op2 = intcodes[c]
        else:
            op2 = 0
        e = op1 + op2
        intcodes[d] = e
        position += 4
    elif op_code == 2:
        if b in intcodes.keys():
            op1 = intcodes[b]
        else:
            op1 = 0
        if c in intcodes.keys():
            op2 = intcodes[c]
        else:
            op2 = 0
        e = op1 * op2
        intcodes[d] = e
        position += 4
    elif op_code == 3:
        intcodes[b] = input_val
        position += 2
    elif op_code == 4:
        if b in intcodes.keys():
            op1 = intcodes[b]
        else:
            op1 = 0
        print(op1)
        position += 2
    elif op_code == 5:
        if b in intcodes.keys():
            op1 = intcodes[b]
        else:
            op1 = 0
        if c in intcodes.keys():
            op2 = intcodes[c]
        else:
            op2 = 0
        if op1 != 0:
            position = op2
        else:
            position += 3
    elif op_code == 6:
        if b in intcodes.keys():
            op1 = intcodes[b]
        else:
            op1 = 0
        if c in intcodes.keys():
            op2 = intcodes[c]
        else:
            op2 = 0
        if op1 == 0:
            position = op2
        else:
            position += 3
    elif op_code == 7:
        if b in intcodes.keys():
            op1 = intcodes[b]
        else:
            op1 = 0
        if c in intcodes.keys():
            op2 = intcodes[c]
        else:
            op2 = 0
        if op1 < op2:
            intcodes[d] = 1
        else:
            intcodes[d] = 0
        position += 4
    elif op_code == 8:
        if b in intcodes.keys():
            op1 = intcodes[b]
        else:
            op1 = 0
        if c in intcodes.keys():
            op2 = intcodes[c]
        else:
            op2 = 0
        if op1 == op2:
            intcodes[d] = 1
        else:
            intcodes[d] = 0
        position += 4
    elif op_code == 9:
        if b in intcodes.keys():
            op1 = intcodes[b]
        else:
            op1 = 0
        relative_base += op1
        position += 2
    else: #Parameter Modes
        str_op = str(op_code)[::-1]
        param_op = int(str_op[0])
        b_mode = 0
        c_mode = 0
        d_mode = 0
        for i in range(2, len(str_op)):
            if i == 2:
                b_mode = int(str_op[i])
            elif i == 3:
                c_mode = int(str_op[i])
            elif i == 4:
                d_mode = int(str_op[i])

        op1 = -1
        op2 = -1
        op3 = -1
        if b_mode == 0:
            if b in intcodes.keys():
                op1 = intcodes[b]
            else:
                op1 = 0
        elif b_mode == 1:
            op1 = b
        else:
            if (b + relative_base) in intcodes.keys():
                op1 = intcodes[b + relative_base]
            else:
                op1 = 0
        if param_op != 3 and param_op != 4 and param_op != 9:
            if c_mode == 0:
                if c in intcodes.keys():
                    op2 = intcodes[c]
                else:
                    op2 = 0
            elif c_mode == 1:
                op2 = c
            else:
                if (c + relative_base) in intcodes.keys():
                    op2 = intcodes[c + relative_base]
                else:
                    op2 = 0
        if param_op == 1:
            e = op1 + op2
            if d_mode == 0:
                intcodes[d] = e
            elif d_mode == 2:
                intcodes[d + relative_base] = e
            position += 4
        elif param_op == 2:
            e = op1 * op2
            if d_mode == 0:
                intcodes[d] = e
            elif d_mode == 2:
                intcodes[d + relative_base] = e
            position += 4
        elif param_op == 3:
            if b_mode == 0:
                intcodes[b] = input_val
            else:
                intcodes[b + relative_base] = input_val
            position += 2
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
                if d_mode == 0:
                    intcodes[d] = 1
                elif d_mode == 2:
                    intcodes[d + relative_base] = 1
            else:
                if d_mode == 0:
                    intcodes[d] = 0
                elif d_mode == 2:
                    intcodes[d + relative_base] = 0
            position += 4
        elif param_op == 8:
            if op1 == op2:
                if d_mode == 0:
                    intcodes[d] = 1
                elif d_mode == 2:
                    intcodes[d + relative_base] = 1
            else:
                if d_mode == 0:
                    intcodes[d] = 0
                elif d_mode == 2:
                    intcodes[d + relative_base] = 0
            position += 4
        elif param_op == 9:
            relative_base += op1
            position += 2