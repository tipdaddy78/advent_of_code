import math
from util.FileHelper import read_file_multiple_lines


def find_fuel(mass):
    return (math.floor(mass / 3) - 2)


lines = read_file_multiple_lines('2019', 'day1')

s = 0

for line in lines:
    cur_sum = 0
    m = int(line.strip())
    while m > 0:
        fuel = find_fuel(m)
        if fuel > 0:
            cur_sum = cur_sum + fuel
        m = fuel
    s = s + cur_sum

print(s)
