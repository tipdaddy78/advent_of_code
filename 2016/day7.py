from util.FileHelper import read_file_multiple_lines

ips = read_file_multiple_lines('2016', 'day7')

tls = 0
ssl = 0

for ip in ips:
    foundAba = False
    foundAbba = False
    abbaSquare = False
    inSquare = False
    babsToFind = list()
    squares = list()
    squareText = ""
    for i in range(len(ip.strip())):
        # Entering a square
        if ip[i] == '[':
            inSquare = True
            squareText = ""
            continue
        # Exiting a square
        elif ip[i] == ']':
            inSquare = False
            squares.append(squareText)
            continue
        if inSquare:
            squareText += ip[i]
        # Looking for ABBAs
        if (i + 3) < (len(ip.strip())):
            cur = ip[i:i+4]
            # Don't want to bother if near the start/end of a bracket
            if cur[0] in ['[', ']']:
                continue
            ab = cur[:2]
            ba = (cur[2:])[::-1]
            if ab[0] != ab[1] and ab == ba:
                if inSquare:
                    abbaSquare = True
                else:
                    foundAbba = True
        # Looking for ABA and BAB
        if (i + 2) < (len(ip.strip())) and not inSquare:
            aba = ip[i:i+3]
            bab = aba[1] + aba[:2]
            if aba[0] == aba[2] and aba[0] != aba[1]:
                babsToFind.append(bab)

    if foundAbba and not abbaSquare:
        tls += 1
    for bab in babsToFind:
        for square in squares:
            if bab in square:
                foundAba = True
                break
        if foundAba:
            break
    if foundAba:
        ssl += 1

print(tls)
print(ssl)


