lines = list()
with open('day2.txt', 'r') as f:
    lines = f.readlines()
    f.close()

checksum = 0
divisionsum = 0
for line in lines:
    numbers = line.split("\t")
    min = 1000000000
    max = 0
    found_divisor = False
    for i in range(len(numbers)):
        n = int(numbers[i])
        if n < min:
            min = n
        if n > max:
            max = n
        if not found_divisor:
            for j in range(len(numbers)):
                n2 = int(numbers[j])
                if n != n2 and n % n2 == 0:
                    divisionsum += (n / n2)
                    found_divisor = True
                    break
    checksum += (max - min)

print(checksum)
print(divisionsum)

