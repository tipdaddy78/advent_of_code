def is_password_valid(pw):
    increasing_straight = False
    pairs = 0
    last_pair_end = -1
    previous_two = ''
    for i in range(len(pw) -1):
        cur = pw[i]
        if cur in {'i', 'o', 'l'}:
            return False
        else:
            next_char = pw[i+1]
            # Finding pairs
            if cur == next_char and i != last_pair_end:
                pairs += 1
                last_pair_end = i + 1
            if i < len(pw) - 2:
                third = pw[i+2]
                if ord(third) - ord(next_char) == 1 and ord(next_char) - ord(cur) == 1:
                    increasing_straight = True
    return increasing_straight and pairs >= 2


def increment_password(pw):
    temp = ''
    pw_reversed = pw[::-1]
    for i in range(len(pw_reversed)):
        n = ord(pw_reversed[i]) - 96
        n = (n + 1) % 26 if n + 1 != 26 else n + 1
        temp += chr(n + 96)
        if n != 1:
            break

    reversed_temp = temp[::-1]
    temp_len = len(temp)
    return pw[:temp_len*-1] + reversed_temp


# pwd = "hepxcrrq" # Part 1
pwd = increment_password("hepxxyzz") # Part 2


while not is_password_valid(pwd):
    pwd = increment_password(pwd)

print(pwd)

