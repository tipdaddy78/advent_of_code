cubes = list()
with open('day2.txt', 'r') as f:
    cubes = f.readlines()
    f.close()

paper_sum = 0
ribbon_sum = 0
for c in cubes:
    smallest = 9999999
    dims = [int(d) for d in c.strip().split('x')]
    dims.sort()
    if len(dims) > 1:
        l = dims[0]
        w = dims[1]
        h = dims[2]
        if l * w < smallest:
            smallest = l * w
        if l * h < smallest:
            smallest = l * h
        if w * h < smallest:
            smallest = w * h
        paper_sum += 2 * l * w + 2 * w * h + 2 * h * l + smallest
        ribbon_sum += 2 * dims[0] + 2 * dims[1] + l * w * h
print(str(paper_sum) + " sq. feet of Wrapping paper needed")
print(str(ribbon_sum) + " sq. feet of ribbon needed")

