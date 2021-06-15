import math

def find_fuel(mass):
    return (math.floor(mass / 3) - 2)

lines = list()
with open('day1.txt', 'r') as f:
    lines = f.readlines()
    f.close()

sum = 0

for line in lines:
    cur_sum = 0
    mass = int(line.strip())
    while mass > 0:
        fuel = find_fuel(mass)
        if fuel > 0 :
            cur_sum = cur_sum + fuel
        mass = fuel
    sum = sum + cur_sum

print(sum)