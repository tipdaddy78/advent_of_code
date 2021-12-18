with open('input/day6.txt', 'r') as f:
    orbits = f.readlines()
    f.close()

orb_dict = dict()

for orbit in orbits:
    parts = orbit.strip().split(')')
    orb_dict[parts[1]] = parts[0]

total_orbits = 0
for key in orb_dict:
    end = 'COM'
    cur = key
    while cur != end:
        total_orbits += 1
        cur = orb_dict[cur]

end = 'COM'
cur = 'YOU'

you_path_to_com = list()
san_path_to_com = list()

while cur != end:
    you_path_to_com.append(cur)
    cur = orb_dict[cur]

cur = 'SAN'
while cur != end:
    san_path_to_com.append(cur)
    cur = orb_dict[cur]

steps = 0
meet = ''
for i in range(1, len(you_path_to_com)):
    if you_path_to_com[i] in san_path_to_com:
        meet = you_path_to_com[i]
        steps = i - 1
        break

steps += (san_path_to_com.index(meet) - 1)

print(steps)
