from util.FileHelper import read_file_multiple_lines

instructions = read_file_multiple_lines('2016', 'day12')

idx = 0
registers = dict()
# Uncomment line below and run for part 2
registers['c'] = 1

while idx < len(instructions):
    i = instructions[idx]
    parts = i.strip().split(' ')
    match parts[0].strip():
        case "cpy":
            if parts[1].isnumeric():
                registers[parts[2]] = int(parts[1])
            else:
                registers[parts[2]] = registers.get(parts[1], 0)
        case "inc":
            registers[parts[1]] = registers.get(parts[1], 0) + 1
        case "dec":
            registers[parts[1]] = registers.get(parts[1], 0) - 1
        case "jnz":
            val = 0
            if parts[1].isnumeric():
                val = int(parts[1])
            else:
                val = registers.get(parts[1], 0)
            if val != 0:
                idx += int(parts[2])
                continue
    idx += 1

print(registers['a'])

