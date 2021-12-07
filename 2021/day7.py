import sys

from util.FileHelper import read_file_single_line

crabs = list()
data = read_file_single_line('2021', 'day7')
for d in data.strip().split(','):
    crabs.append(int(d))

least = min(crabs)
most = max(crabs)
best_fuel_used = sys.maxsize
best_fuel_space = 0
best_fuel_used2 = sys.maxsize
best_fuel_space2 = 0
# For part 2 to prevent multiple calculations
distances = dict()
# Loop over smallest position to largest position
# f indicates the destination position for crabs
for f in range(least, most+1):
    fuel_used = 0
    fuel_used2 = 0
    for c in crabs:
        fuel_used += abs(f - c)
        # Part 2
        if f == 5:
            x = 2
        if distances.get(abs(f-c)):
            fuel_used2 += distances.get(abs(f-c))
        else:
            # Calculate the fuel needed for this distance
            i = 1  # current number to add to fuel sum
            s = 0  # fuel sum
            for j in range(min(f, c), max(f, c)):
                s += i
                i += 1
            fuel_used2 += s
            distances[abs(f-c)] = s
    if fuel_used < best_fuel_used:
        best_fuel_used = fuel_used
        best_fuel_space = f
    if fuel_used2 < best_fuel_used2:
        best_fuel_used2 = fuel_used2
        best_fuel_space2 = f


print(best_fuel_used)
print(best_fuel_space)
print(best_fuel_used2)
print(best_fuel_space2)
