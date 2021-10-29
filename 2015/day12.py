from util.FileHelper import read_json_file


def traverse_json_dict(j, s, pt2=False):
    for key in j.keys():
        t = type(j[key])
        if t is dict:
            s += traverse_json_dict(j[key], 0, pt2)
        elif t is list:
            s += traverse_json_list(j[key], 0, pt2)
        elif t is int:
            s += j[key]
        elif t is str and pt2 and j[key] == 'red':
            return 0
    return s


def traverse_json_list(j, s, pt2=False):
    for item in j:
        t = type(item)
        if t is dict:
            s += traverse_json_dict(item, 0, pt2)
        elif t is list:
            s += traverse_json_list(item, 0, pt2)
        elif t is int:
            s += item
    return s


data = read_json_file('2015', 'day12')
total = 0
if type(data) is dict:
    total = traverse_json_dict(data, total)
else:
    total = traverse_json_list(data, total)
print(total)

total = 0
if type(data) is dict:
    total = traverse_json_dict(data, total, True)
else:
    total = traverse_json_list(data, total, True)
print(total)
