data = ""
frequency = 0
numbers_seen = set()
first_dub = 0
found_dub = False
with open('day1.txt', 'r') as f:
    data = f.readlines()
    f.close()


increase = True;
while not found_dub:
    for line in data:
        operator = line[0]
        num = int(line[1:])
        if (operator == '-'):
            frequency = frequency - num
        else:
            frequency = frequency + num
        if frequency in numbers_seen:
            first_dub = frequency
            found_dub = True
            print("Found duplicate!")
            break
        else:
            numbers_seen.add(frequency)

print(frequency)
print(first_dub)
