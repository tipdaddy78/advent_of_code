import math

puzzle_input = list()
with open('day1.txt', 'r') as f:
    puzzle_input = f.readlines()
    f.close()

def get_fuel_for_mass(mass):
    m = mass / 3
    m = math.floor(m)
    m -= 2
    return m

def part1():
    mass_sum = 0
    for line in puzzle_input:
        mass_sum += get_fuel_for_mass(int(line))
    return mass_sum

def part2():
    mass_sum = 0
    for line in puzzle_input:
        curr = int(line)
        while get_fuel_for_mass(curr) > 0:
            next = get_fuel_for_mass(curr)
            mass_sum += next
            curr = next
    return mass_sum

print("Part 1: " + str(part1()))
print("Part 2: " + str(part2()))