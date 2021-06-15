def react(poly):
    new_poly = list()
    last = ''
    for letter in poly:
        if len(new_poly) == 0:
            new_poly.append(letter)
        else:
            last = new_poly[len(new_poly)-1]
            if (last.islower() and last.capitalize() == letter) or (last.isupper() and last.lower() == letter):
                new_poly.pop()
            else:
                new_poly.append(letter)
    return(len(new_poly))

first_poly = ''
with open('day5.txt', 'r') as f:
    first_poly = f.read().strip()
    f.close()

print(react(first_poly))

letters = set([c.lower() for c in first_poly])
poly_lengths = list()
for l in letters:
    replaced_poly = first_poly.replace(l, '').replace(l.upper(), '')
    poly_lengths.append((react(replaced_poly)))


print(min(poly_lengths))


