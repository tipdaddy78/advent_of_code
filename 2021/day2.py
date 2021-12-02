from util.FileHelper import read_file_multiple_lines

sub_course = read_file_multiple_lines('2021', 'day2')

x = 0
x_2 = 0
depth = 0
depth_2 = 0
aim = 0

for sc in sub_course:
    parts = sc.strip().split(' ')
    match parts[0]:
        case 'forward':
            x += int(parts[1])
            x_2 += int(parts[1])
            depth_2 += (aim * int(parts[1]))
        case 'down':
            depth += int(parts[1])
            aim += int(parts[1])
        case 'up':
            depth -= int(parts[1])
            aim -= int(parts[1])

print(x * depth)
print(x_2 * depth_2)
