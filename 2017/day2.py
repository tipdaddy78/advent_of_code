lines = list()
checksum = 0
with open('day2.txt', 'r') as f:
    lines = f.readlines()
    f.close()

for line in lines:
    numbers = line.split("\t")
    breakI = False
    min = 1000000000
    max = 0
    for i in range(len(numbers)):

        # num1 = int(numbers[i])
        # for j in range(len(numbers)):
        #     if (i == j):
        #         continue
        #     num2 = int(numbers[j])
        #     test = num1 / num2
        #     if (test == int(test)):
        #         checksum += test
        #         breakI = True
        #         break
        # if (breakI):
        #     break

print(checksum)

