class Range:
    def __init__(self, min=0, max=0):
        self.min = min
        self.max = max

class Rule:
    def __init__(self, id = '', ranges = list()):
        self.id = id
        self.ranges = list()
        for ra in ranges:
            r = Range(ra[0], ra[1])
            self.ranges.append(r)

    def is_valid(self, v):
        for r in self.ranges:
            if r.min <= v and v <= r.max:
                return True
        return False

class TicketSystem:
    def __init__(self):
        self.rules = dict()
        self.v_tix = list()
        self.rule_ids = dict()

    def add_rule(self, rule = ''):
        parts = rule.split(':')
        r_id = parts[0].strip()
        ranges = list()
        parts2 = parts[1].split('or')
        nbr = len(self.rules)
        for p in parts2:
            ranges.append((int(p.split('-')[0].strip()), int(p.split('-')[1].strip())))
        self.rules[r_id] = (Rule(r_id, ranges))

    def validate_ticket(self, ticket=list()):
        errors = list()
        for t in ticket:
            valid = False
            for r in self.rules.keys():
                for r2 in self.rules[r].ranges:
                    if int(t) >= r2.min and int(t) <= r2.max:
                        valid = True
                if valid:
                    break
            if not valid:
                errors.append(int(t))
        if len(errors) == 0:
            self.v_tix.append(ticket)
        return errors

    def identify_rules(self):
        id_dict = dict()
        nbr_rules = len(self.rules)
        for r in self.rules.keys():
            id_dict[r] = [i for i in range(nbr_rules)]
        searching = True
        i = 0
        inv_dict = dict()
        completed = list()
        for j in range(nbr_rules):
            inv_dict[j] = list()
        while searching:
            # Loop through each rule name
            for k in id_dict.keys():
                ids = id_dict.get(k)
                ru = self.rules.get(k)
                if k not in completed and i in ids:
                    # Try to validate the rule against the ticket
                    for t in self.v_tix:
                        # If a rule is invalid, we should remove the index from possible rule indexes
                        if not ru.is_valid(int(t[i].strip())):
                            # take the index away from the rule.
                            ids.remove(i)
                            # if we have a rule with only one option
                            if len(ids) == 1:
                                x = ids[0]
                                # remove that option from other rules
                                for k2 in id_dict.keys():
                                    ids2 = id_dict.get(k2)
                                    if x in ids2 and k2 != k:
                                        ids2.remove(x)
                                completed.append(k)
                            # Add rule name to list of rules that are invalid for this index.
                            inv_dict[i].append(k)
                            # If we've eliminated all but one possible option
                            if len(inv_dict[i]) == nbr_rules - 1:
                                # find the option that belongs to this rule.
                                for k2 in id_dict.keys():
                                    if k2 not in inv_dict[i]:
                                        # Put an index list with just this option in it.
                                        id_dict[k2] = [i]
                                        break
                else:
                    if len(ids) == 1:
                        x = ids[0]
                        # remove that option from other rules
                        for k2 in id_dict.keys():
                            ids2 = id_dict.get(k2)
                            if x in ids2 and k2 != k:
                                ids2.remove(x)
                        completed.append(k)

            i = (i + 1) % nbr_rules
            # After checking all tickets/rules on the first index
            # Check to see if id lists are all of length 1
            shouldContinue = False
            for k2 in id_dict.keys():
                if len(id_dict[k2]) > 1:
                    shouldContinue = True
                    break
            if not shouldContinue:
                searching = False
        self.rule_ids = id_dict

puzzle_input = list()
with open('day16.txt', 'r') as f:
    puzzle_input = f.readlines()
    f.close()

ts = TicketSystem()
tickets = list()
my_ticket = list()
for i in range(len(puzzle_input)):
    if i < 20:
        ts.add_rule(puzzle_input[i])
    elif i == 22:
        my_ticket = puzzle_input[i].split(',')
    elif i > 24:
        tickets.append(puzzle_input[i].split(','))

def process(ts, tickets, my_ticket):
    # Part 1
    errors = list()
    for t in tickets:
        errors += ts.validate_ticket(t)
    e_sum = 0
    for e in errors:
        e_sum += e
    print("Part 1 Answer: " + str(e_sum))

    # Part 2
    ts.identify_rules()
    m_mult = 1
    for k in ts.rule_ids.keys():
        if 'departure' in k:
            m_mult *= int(my_ticket[ts.rule_ids.get(k)[0]].strip())
    print("Part 2 Answer: " + str(m_mult))

process(ts, tickets, my_ticket)





