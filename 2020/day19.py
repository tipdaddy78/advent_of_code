lines = list()
with open('day19.txt', 'r') as f:
    lines = [line.strip() for line in f]
    f.close()

class Rule:
    def __init__(self, id):
        self.id = id
        self.values = list()
        self.subs = list()

    def append_value(self, value):
        self.values.append(value)

    def append_sub(self, sub):
        self.subs.append(sub)

rules = dict()
def get_rules():
    for line in lines:
        if line == '':
            break
        parts = line.split(':')
        id = parts[0].strip()
        rule = Rule(id)
        if '\"' in parts[1]:
            value = parts[1].replace('\"', '').strip()
            rule.append_value(value)
        elif '|' in parts[1]:
            subs = parts[1].strip().split('|')
            for sub in subs:
                s = sub.strip().split(' ')
                rule.append_sub(s)
        else:
            sub = parts[1].strip().split(' ')
            rule.append_sub(sub)
        rules[id] = rule
    return rules

def get_values():
    values = list()
    for line in lines:
        if ':' in line or line == '':
            continue
        else:
            values.append(line.strip())
    return values

def get_valid_strings(id, values, loop_mode):
    rule = rules.get(id)
    dup = values.copy()
    if len(rule.values) != 0:
        if len(dup) == 0:
            dup.append(rule.values[0])
        else:
            for i in range(len(dup)):
                v = dup[i]
                v += rule.values[0]
                dup[i] = v
        return dup
    else:
        if len(rule.subs) == 1:
            for s in rule.subs[0]:
                if not loop_mode:
                    if s == '8':
                        if len(dup) == 0:
                            dup.append('X')
                        else:
                            for i in range(len(dup)):
                                v = dup[i]
                                v += 'X'
                                dup[i] = v
                    elif s == '11':
                        if len(dup) == 0:
                            dup.append('Y')
                        else:
                            for i in range(len(dup)):
                                v = dup[i]
                                v += 'Y'
                                dup[i] = v
                else:
                    dup = get_valid_strings(s, dup, loop_mode)
            return dup
        else:
            new_values = list()
            final = list()
            for sub in rule.subs:
                new_values = dup.copy()
                for s in sub:
                    new_values = get_valid_strings(s, new_values, loop_mode)
                final.extend(new_values)
            return final

def run(m):
    global rules
    rules = get_rules()
    values = get_values()
    matches = list()
    count = 0
    if m == 1:
        valid = get_valid_strings('0', list(), True)
        for v in values:
            if v in valid:
                matches.append(v)
                count += 1
    else:
        valid42 = get_valid_strings('42', list(), True)
        valid31 = get_valid_strings('31', list(), True)
        print(valid42)
        print(valid31)
        idx_len = len(valid42[0])
        for value in values:
            # Loop in slices of the current line.
            end_i = len(value)
            start_i = end_i - idx_len
            middle_i = -1
            v_31 = False
            l_31 = list()
            l_42 = list()
            while start_i >= 0:
                # start from the back and work to some middle point
                cur = value[start_i : end_i]
                # back portion of strings should match something in 31's valid list
                if cur in valid31:
                    end_i -= idx_len
                    start_i -= idx_len
                    l_31.insert(0, cur)
                    continue
                else:
                    # no match means we've met the matches to 42
                    if cur in valid42:
                        middle_i = end_i
                        v_31 = True
                        break
                    # no match on 42 as well means it's not a valid string.
                    else:
                        break
            # middle_i being -1 or the end of the string means we never matched with 31 and string isn't valid
            if middle_i in [-1, len(value)] or not v_31:
                continue
            # start again but from beginning of the string
            start_i = 0
            end_i = idx_len
            v_42 = True
            while end_i <= middle_i:
                # get current slice and see if it's in 42 set.
                cur = value[start_i : end_i]
                if cur in valid42:
                    start_i += idx_len
                    end_i += idx_len
                    l_42.append(cur)
                    continue
                else:
                    v_42 = False
                    break
            # if it found matches all the way up to the mid point, end_i should be idx_len values greater than middle_i
            # due to rules, there should be more matches to rule 42 than to 31.
            if v_31 and v_42 and len(l_42) > len(l_31):
                print("Cur: " + value + " has a length of: " + str(len(value)))
                print(l_42)
                print(l_31)
                matches.append(value)
                count += 1
    print(matches)
    return count





# print(run(1))
print(run(2))