lines = list()
with open('day19_test.txt', 'r') as f:
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
    if m == 1:
        valid = get_valid_strings('0', list(), True)
    else:
        valid = get_valid_strings('0', list(), False)
        print(valid)
    valid2 = get_valid_strings('42', list(), True)
    valid3 = get_valid_strings('31', list(), True)
    print(valid2)
    print(valid3)
    count = 0
    for v in values:
        if v in valid:
            matches.append(v)
            count += 1
    print(matches)
    return count

print(run(1))
print(run(2))