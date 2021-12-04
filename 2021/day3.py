from util.FileHelper import read_file_multiple_lines

data = read_file_multiple_lines('2021', 'day3')
length = len(data[0].strip())


def get_bit_counts(strings, index=-1):
    bit_counts = dict()
    for string in strings:
        b_string = string.strip()
        if index == -1:
            for j in range(len(b_string)):
                b_counts = bit_counts.get(j, [0, 0])
                if b_string[j] == '0':
                    b_counts[0] += 1
                else:
                    b_counts[1] += 1
                bit_counts[j] = b_counts
        else:
            b_counts = bit_counts.get(index, [0, 0])
            if b_string[index] == '0':
                b_counts[0] += 1
            else:
                b_counts[1] += 1
            bit_counts[index] = b_counts
    return bit_counts


gamma = ''
epsilon = ''
p1 = get_bit_counts(data)

for i in range(length):
    b_c = p1.get(i)
    if b_c[0] > b_c[1]:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

print(int(gamma, 2) * int(epsilon, 2))

# Part 2
oxygen_list = data.copy()
co2_list = data.copy()
for i in range(length):
    new_oxy = list()
    new_co2 = list()
    if len(oxygen_list) > 1:
        oxy_counts = get_bit_counts(oxygen_list, i)
        # filter oxy_list
        oxy_i_count = oxy_counts.get(i)
        if oxy_i_count[0] > oxy_i_count[1]:
            new_oxy = list(filter(lambda o: o[i] == '0', oxygen_list))
        else:
            new_oxy = list(filter(lambda o: o[i] == '1', oxygen_list))
        oxygen_list = new_oxy
    if len(co2_list) > 1:
        co2_counts = get_bit_counts(co2_list, i)
        # filter oxy_list
        co2_i_count = co2_counts.get(i)
        if co2_i_count[0] < co2_i_count[1] or co2_i_count[0] == co2_i_count[1]:
            new_co2 = list(filter(lambda c: c[i] == '0', co2_list))
        else:
            new_co2 = list(filter(lambda c: c[i] == '1', co2_list))
        co2_list = new_co2

print(int(oxygen_list[0], 2) * int(co2_list[0], 2))
