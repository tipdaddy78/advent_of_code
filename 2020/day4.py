puzzle_input = list()
with open('day4.txt', 'r') as f:
    puzzle_input = f.readlines()
    f.close()

BYR_KEY = 'byr'
IYR_KEY = 'iyr'
EYR_KEY = 'eyr'
HGT_KEY = 'hgt'
HCL_KEY = 'hcl'
ECL_KEY = 'ecl'
PID_KEY = 'pid'
CID_KEY = 'cid'

class Passport:
    def __init__(self):
        self.attributes = dict()

    def add_attribute(self, key, value):
        self.attributes[key] = value

    def is_valid(self, part):
        has_keys = False
        if (BYR_KEY in self.attributes.keys()) \
                and IYR_KEY in self.attributes.keys() \
                and EYR_KEY in self.attributes.keys() \
                and HGT_KEY in self.attributes.keys() \
                and HCL_KEY in self.attributes.keys() \
                and ECL_KEY in self.attributes.keys() \
                and PID_KEY in self.attributes.keys():
            has_keys = True
        else:
            return False
        if part == 1 and has_keys:
            return True
        if has_keys:
            #BYR Validation
            byr = int(self.attributes.get(BYR_KEY))
            if byr < 1920 or byr > 2002:
                return False
            #IYR Validation
            iyr = int(self.attributes.get(IYR_KEY))
            if iyr < 2010 or iyr > 2020:
                return False
            #EYR Validation
            eyr = int(self.attributes.get(EYR_KEY))
            if eyr < 2020 or eyr > 2030:
                return False
            #HGT Validation
            hgt_val = self.attributes.get(HGT_KEY)[:-2]
            hgt_typ = self.attributes.get(HGT_KEY)[-2:]
            if hgt_typ == 'cm':
                if not hgt_val.isnumeric() \
                    or int(hgt_val) < 150 \
                    or int(hgt_val) > 193:
                    return False
            elif hgt_typ == 'in':
                if not hgt_val.isnumeric() \
                    or int(hgt_val) < 59 \
                    or int(hgt_val) > 76:
                    return False
            else:
                return False
            #HCL Validation
            hcl_val = self.attributes.get(HCL_KEY)
            if hcl_val[0] != '#' or len(hcl_val) != 7:
                return False
            for i in range(1, len(hcl_val)):
                if hcl_val[i] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']:
                    return False
            #ECL Validation
            ecl_val = self.attributes.get(ECL_KEY)
            if len(ecl_val) > 3 or \
                ecl_val not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                return False
            #PID Validation
            pid_val = self.attributes.get(PID_KEY)
            if len(pid_val) != 9 or not pid_val.isnumeric():
                return False
        return True

passports = list()
create_new = True
pass_p = None
for p in puzzle_input:
    if create_new:
        pass_p = Passport()
        create_new = False
    if p.strip() == '':
        create_new = True
        passports.append(pass_p)
        pass_p = None
        continue
    attributes = p.split(' ')
    for a in attributes:
        key = a.split(':')[0].strip()
        value = a.split(':')[1].strip()
        pass_p.add_attribute(key, value)

if pass_p != None:
    passports.append(pass_p)

def part1():
    count = 0
    for pp in passports:
        if pp.is_valid(1):
            count += 1
    return count

def part2():
    count = 0
    for pp in passports:
        if pp.is_valid(2):
            count += 1
    return count


print(part1())
print(part2())
