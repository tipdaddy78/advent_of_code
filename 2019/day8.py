with open('input/day8.txt', 'r') as f:
    image = f.read().strip()
    f.close()

#image = '0222112222120000'
width = 25
#width = 2
height = 6
#height = 2

layers = list()
layer = [[0 for i in range(width)] for j in range(height)]
x = 0
y = 0
for px in image:
    layer[y][x] = int(px)
    x = (x + 1) % width
    if x == 0:
        y = (y + 1) % height
        if y == 0:
            layers.append(layer.copy())
            layer = [[0 for i in range(width)] for j in range(height)]

final_image = [[0 for i in range(width)] for j in range(height)]

for i in range(width):
    for j in range(height):
        for k in range(len(layers)):
            cur = layers[k][j][i]
            if cur == 1 or cur == 0:
                final_image[j][i] = cur
                break

for line in final_image:
    print(line)

