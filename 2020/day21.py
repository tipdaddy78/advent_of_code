pos_ing = set()
i_d = dict()
class Allergen:
    def __init__(self, name):
        self.name = name
        self.ingredients = dict()

    def increment_ingredient(self, key):
        if key not in self.ingredients.keys():
            self.ingredients[key] = 1
        else:
            self.ingredients[key] += 1

    def narrow_list(self):
        d = dict()
        m = max(self.ingredients.values())
        for k in self.ingredients.keys():
            if self.ingredients[k] == m:
                d[k] = self.ingredients[k]
        self.ingredients = d

    def remove_key(self, key):
        if key in self.ingredients.keys():
            self.ingredients.pop(key)

def parse_input():
    lines = list()
    with open('day21.txt', 'r') as f:
        lines = [line.strip() for line in f]

    a_d = dict()
    for line in lines:
        parts = line.replace(')', '').split(' (contains ')
        ingredients = parts[0].split(' ')
        allergens = parts[1].split(', ')
        for allg in allergens:
            if allg in a_d.keys():
                a = a_d[allg]
            else:
                a = Allergen(allg)
            for i in ingredients:
                pos_ing.add(i)
                a.increment_ingredient(i)
                if i in i_d.keys():
                    i_d[i] += 1
                else:
                    i_d[i] = 1
            a_d[allg] = a
    return a_d

def solve(allergens = dict()):
    narrowing = True
    matching = set(allergens.keys())
    matches = set()
    while narrowing:
        for k in matching:
            new_matching = matching.copy()
            a = allergens[k]
            l = len(a.ingredients)
            if l == 1:
                # found a match
                i = list(a.ingredients.keys())[0]
                if i in pos_ing:
                    pos_ing.remove(i)
                new_matching.remove(k)
                for allg in allergens.keys():
                    a2 = allergens[allg]
                    if a2.name != a.name:
                        a2.remove_key(i)
            else:
                a.narrow_list()
        matched = True

        for k in allergens.keys():
            if len(allergens[k].ingredients) > 1:
                matched = False
                break
            else:
                matches.add(list(allergens[k].ingredients.keys())[0])
        if matched:
            narrowing = False
        else:
            matches.clear()
            matching = new_matching
    count = 0
    for p in pos_ing:
        count += i_d.get(p)
    return count




def run():
    global pos_ing, i_d
    pos_ing = set()
    i_d = dict()
    a_d = parse_input()
    return solve(a_d)

print(run())