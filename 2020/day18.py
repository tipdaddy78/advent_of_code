lines = list()
with open('day18.txt', 'r') as f:
    lines = [line.strip() for line in f]
    f.close()

def solve_problem(mode, prob_string, new_prob, start, i, end, total, num, op):
    # go character by character
    if i < end:
        cur = prob_string[i]
        if cur.isnumeric():
            # starting number
            if total == -1:
                total = int(cur)
            else:
                num = int(cur)
        elif cur == '(':
            s = i
            e = find_closing_paren(prob_string, s+1)
            sub = prob_string[s+1:e]
            temp = solve_problem(mode, sub, list(), 0, 0, len(sub), -1, -1, '')
            # n_p = prob_string[:s] + str(temp) + prob_string[e+1:]
            if total == -1:
                total = temp
            else:
                num = temp
            i = e
        elif cur in ['*', '+']:
            op = cur
        if num != -1 and op != '':
            if op == '+':
                if mode == 2:
                    if len(new_prob) > 0:
                        temp = int(new_prob[-1]) + num
                        new_prob = new_prob[:-1]
                        new_prob.append(str(temp))
                    else:
                        new_prob = [str(total + num)]
                else:
                    total += num
            else:
                if mode == 2:
                    if '+' not in prob_string:
                        total *= num
                    else:
                        if len(new_prob) == 0:
                            new_prob.append(str(total))
                        new_prob.append(op)
                        new_prob.append(str(num))

                else:
                    total *= num
            # reset  so no duplicate operations
            num = -1
            op = ''
        return solve_problem(mode, prob_string, new_prob, start, i + 1, end, total, num, op)
    else:
        if mode == 2:
            if '+' in new_prob or '*' in new_prob:
                return solve_problem(mode, new_prob, '', 0, 0, len(new_prob), -1, -1, '')
            elif len(new_prob) == 1:
                return int(new_prob[0])
            else:
                return total
        else:
            return total

def find_closing_paren(prob_string, start):
    level = 1
    for i in range(start, len(prob_string)):
        if prob_string[i] == '(':
            level += 1
        elif prob_string[i] == ')':
            level -= 1
            if level == 0:
                return i
    #didn't find a closing paren
    return -1

def get_prob_list(prob):
    ret = list()
    temp = prob.split(' ')
    for t in temp:
        if len(t) == 1:
            ret.append(t)
        else:
            for c in t:
                ret.append(c)
    return ret

sum = 0
for line in lines:
    l = get_prob_list(line)
    sum += solve_problem(1, l, list(), 0, 0, len(l), -1, -1, '')
print(sum)

sum = 0
for line in lines:
    l = get_prob_list(line)
    sum += solve_problem(2, l, list(), 0, 0, len(l), -1, -1, '')
print(sum)
