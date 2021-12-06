from util.FileHelper import read_file_single_line

data = read_file_single_line('2021', 'day6').strip().split(',')
f_dict = dict()
for d in data:
    f_dict[int(d)] = f_dict.get(int(d), 0) + 1

# part 1 is 80 days, part 2 = 256
for x in range(256):
    new_dict = dict()
    for k in f_dict.keys():
        if k == 0:
            new_dict[8] = f_dict[k]
            new_dict[6] = new_dict.get(6, 0) + f_dict[k]
        else:
            new_dict[k-1] = new_dict.get(k-1, 0) + f_dict[k]
    f_dict = new_dict

print(sum(f_dict.values()))
