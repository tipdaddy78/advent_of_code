from util.FileHelper import read_file_multiple_lines

t_dimensions = read_file_multiple_lines("2016", "day3")


def is_valid_triangle(side1, side2, side3):
    return (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1)


# Part 1
possible = 0

for line in t_dimensions:
    d1 = int(line[0:5])
    d2 = int(line[6:10])
    d3 = int(line[11:15])
    if is_valid_triangle(d1, d2, d3):
        possible += 1
print(possible)

# Part 2
# This part forces you to read triangle dimensions via columns instead of by row.
# I accomplish this using a loop that reads 3 lines (hence three triangles) at a time
possible = 0
l = 0
for i in range(int(len(t_dimensions) / 3)):
    t1d1 = int(t_dimensions[l][0:5])
    t2d1 = int(t_dimensions[l][6:10])
    t3d1 = int(t_dimensions[l][11:15])
    t1d2 = int(t_dimensions[l+1][0:5])
    t2d2 = int(t_dimensions[l+1][6:10])
    t3d2 = int(t_dimensions[l+1][11:15])
    t1d3 = int(t_dimensions[l+2][0:5])
    t2d3 = int(t_dimensions[l+2][6:10])
    t3d3 = int(t_dimensions[l+2][11:15])

    if is_valid_triangle(t1d1, t1d2, t1d3):
        possible += 1
    if is_valid_triangle(t2d1, t2d2, t2d3):
        possible += 1
    if is_valid_triangle(t3d1, t3d2, t3d3):
        possible += 1

    l += 3
print(possible)
