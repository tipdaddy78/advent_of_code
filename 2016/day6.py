from util.FileHelper import read_file_multiple_lines

errors = read_file_multiple_lines('2016', 'day6')

d_index = dict()


for error in errors:
    for i in range(len(error.strip())):
        i_dict = d_index.get(i, dict())
        i_dict[error[i]] = i_dict.get(error[i], 0) + 1
        d_index[i] = i_dict

password_1 = ''
password_2 = ''

for index in d_index.keys():
    ordered = dict(sorted(d_index.get(index).items(), key=lambda item: item[1], reverse=True))
    for key in ordered.keys():
        password_1 += key
        break
    password_2 += ordered.popitem()[0]

print("Part 1 Password:", password_1)
print("Part 2 Password:", password_2)

