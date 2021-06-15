import math

class material:
    def __init__(self, id, amount, ingredients):
        self.id = id
        self.amount = amount
        self.ingredients = ingredients

def get_needs(material_id, amount_needed, material_dict, needed_dict, leftover_dict):
    m = material_dict.get(material_id)
    if len(m.ingredients) == 1 and m.ingredients[0][0] == 'ORE':
        new_needed = dict()
        material = material_dict.get(material_id)
        new_needed[material_id] = amount_needed
        return new_needed
    else:
        for i in m.ingredients:
            new_needed = get_needs(i[0], i[1], material_dict, needed_dict, leftover_dict)
            old = needed_dict.get(i[0])
            cur = new_needed.get(i[0])
            leftover = leftover_dict.get(i[0])
            if cur is not None:
                cur *= math.ceil(amount_needed / m.amount)
                if old is not None:
                    needed_dict[i[0]] = cur + old
                else:
                    needed_dict[i[0]] = cur
        return needed_dict

def get_needs_new(material_id, amount_needed, material_dict, needed_dict, leftover_dict):
    m = material_dict.get(material_id)
    if len(m.ingredients) == 1 and m.ingredients[0][0] == 'ORE':
        new_needed = dict()
        new_needed[material_id] = amount_needed * m.amount
        return new_needed
    else:
        for i in m.ingredients:
            cur_left = leftover_dict.get(i[0])
            if cur_left is not None:
                amt_still_needed = (amount_needed * i[1]) - cur_left
                if amt_still_needed < 0:
                    leftover_dict[i[0]] = abs(amt_still_needed)
                    new_amt = 0
                elif amt_still_needed == 0:
                    new_amt = 0
                else:
                    leftover_dict.pop(i[0])
                    new_amt = math.ceil(amt_still_needed / material_dict.get(i[0]).amount)
            else:
                new_amt = math.ceil((amount_needed * i[1]) / material_dict.get(i[0]).amount)
            if new_amt != 0:
                new_needed = get_needs_new(i[0], new_amt, material_dict, needed_dict, leftover_dict)
                old = needed_dict.get(i[0])
                cur = new_needed.get(i[0])
                leftover = 0
                if cur is not None:
                    leftover = cur % (amount_needed * i[1])
                    if old is not None:
                        needed_dict[i[0]] = cur + old
                    else:
                        needed_dict[i[0]] = cur
                if leftover != 0:
                    leftover_dict[i[0]] = leftover
        return needed_dict

def get_ore(needed_dict, material_dict):
    total = 0
    for k in needed_dict.keys():
        needed = needed_dict.get(k)
        material = material_dict.get(k)
        total += (math.ceil(needed / material.amount) * material.ingredients[0][1])
    return total

# with open('day14.txt', 'r') as f:
#     data = f.readlines()
#     f.close()
#
# data = [
# '9 ORE => 2 A',
# '8 ORE => 3 B',
# '7 ORE => 5 C',
# '3 A, 4 B => 1 AB',
# '5 B, 7 C => 1 BC',
# '4 C, 1 A => 1 CA',
# '2 AB, 3 BC, 4 CA => 1 FUEL'
# ]

data = [
    '157 ORE => 5 NZVS',
    '165 ORE => 6 DCFZ',
    '44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL',
    '12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ',
    '179 ORE => 7 PSHF',
    '177 ORE => 5 HKGWZ',
    '7 DCFZ, 7 PSHF => 2 XJWVT',
    '165 ORE => 2 GPVTF',
    '3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT'
]

# data = [
# '2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG',
# '17 NVRVD, 3 JNWZP => 8 VPVL',
# '53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL',
# '22 VJHF, 37 MNCFX => 5 FWMGM',
# '139 ORE => 4 NVRVD',
# '144 ORE => 7 JNWZP',
# '5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC',
# '5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV',
# '145 ORE => 6 MNCFX',
# '1 NVRVD => 8 CXFTF',
# '1 VJHF, 6 MNCFX => 4 RFSQX',
# '176 ORE => 6 VJHF'
# ]

materials = dict()
for reaction_string in data:
    reaction_info = reaction_string.strip().split('=>')
    result_info = reaction_info[1].strip().split(' ')
    ingredient_info = reaction_info[0].strip().split(',')
    ingredients = list()
    for ingredient in ingredient_info:
        info = ingredient.strip().split(' ')
        ingredients.append((info[1].strip(), int(info[0].strip())))
    m = material(result_info[1].strip(), int(result_info[0].strip()), ingredients)
    materials[m.id] = m

x = math.ceil(17 / 6)

needed = dict()
leftovers = dict()
needed = get_needs("FUEL", 1, materials, needed, leftovers)
ore = get_ore(needed, materials)
print(ore)