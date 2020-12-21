import time

current_milli_time = lambda: int(round(time.time() * 1000))


def react(poly):
    new_poly = list()
    last = ''
    for letter in poly:
        if len(new_poly) == 0:
            new_poly.append(letter)
        else:
            last = new_poly[len(new_poly)-1]
            if (last.islower() and last.capitalize() == letter) or (last.isupper() and last.lower() == letter):
                new_poly.pop()
            else:
                new_poly.append(letter)
    return(len(new_poly))

start = current_milli_time()
poly1 = ''
with open('day5.txt', 'r') as f:
    poly1 = f.read().strip()
    f.close()

leng = react(poly1)
mid = current_milli_time()
print("time taken for part 1: " + str(mid - start))

alpha = "abcdefghijklmnopqrstuvwxyz"
lengths = list()
for a in alpha:
    reduced_poly = poly1.replace(a, '').replace(a.upper(), '')
    length = react(reduced_poly)
    lengths.append(length)


print(min(lengths))
end = current_milli_time()
print("time taken for part 1: " + str(end - mid))
