input = 880751
scores = [3, 7]
elf1 = 0
elf2 = 1
blah = [8,8,0,7,5,1]

while True:
    e1 = scores[elf1]
    e2 = scores[elf2]
    recipe = str(e1 + e2)
    scores.extend(map(int, recipe))
    elf1 = (elf1 + e1 + 1) % len(scores)
    elf2 = (elf2 + e2 + 1) % len(scores)
    if len(scores) == input + 10:
        print(scores[-10:])
    if scores[-len(blah):] == blah or scores[-len(blah) - 1:-1] == blah:
        break

if scores[-len(blah):] == blah:
    print(len(scores) - len(blah))
else:
    print(len(scores) - len(blah) - 1)

print(scores[input:input+10])
