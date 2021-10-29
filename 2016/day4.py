from util.FileHelper import read_file_multiple_lines


def decrypt_character(orig, sector):
    if sector == 379:
        x = 2
    shift = sector % 26
    start = ord(orig) - 96
    end = (start + shift) % 26 if start + shift != 26 else start + shift
    return chr(end + 96)


rooms = read_file_multiple_lines("2016", "day4")
total = 0

for room in rooms:
    parts = room.strip().split("-")
    roomName = parts[:-1]
    other = parts[-1]
    check = other.split('[')[1][:-1]
    sector = int(other.split('[')[0])

    counts = dict()
    for word in roomName:
        for letter in word:
            counts[letter] = counts.get(letter, 0) + 1

    # Sort the occurrence dictionary
    ordered = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))

    # Build the correct checksum
    my_check = ""
    last = 0
    level = list()
    for x in ordered.keys():
        cur = ordered.get(x)
        if cur != last:
            # Got to the next level, load in previous level
            if len(level) != 0:
                s_level = sorted(level)
                for l in s_level:
                    my_check += l
                    if len(my_check) == 5:
                        break
                level.clear()
        level.append(x)
        last = cur
        if len(my_check) == 5:
            break

    # Got to end of sorted list and don't have an ID yet.
    if len(my_check) != 5:
        s_level = sorted(level)
        for l in s_level:
            my_check += l
            if len(my_check) == 5:
                break

    # room is valid
    if check == my_check:
        total += sector
        # Decrypt the room name.
        newName = list()
        for word in roomName:
            newWord = ''
            for letter in word:
                newWord += decrypt_character(letter, sector)
            newName.append(newWord)
        print("Room:", newName, "is located in sector:", sector)

print("Part 1 Answer:", total)
