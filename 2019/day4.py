lower_bound = 264793
upper_bound = 803935


def valid_pass(pwd):
    has_double = False
    always_inc = True
    for i in range(len(pwd)-1):
        p = int(pwd[i])
        p1 = int(pwd[i+1])
        if p == p1:
            has_double = True
        if p > p1:
            always_inc = False
            break
    if has_double and always_inc:
        return True
    return False


def valid_pass2(pwd):
    has_double = False
    always_inc = True
    i = 0
    while i < len(pwd) - 1:
        p = int(pwd[i])
        p1 = int(pwd[i+1])
        if p == p1:
            j = i + 2
            while j < len(pwd):
                if int(pwd[j]) == p:
                    j += 1
                else:
                    break
            if j == (i + 2):
                has_double = True
            i = j - 1
        else:
            if p > p1:
                always_inc = False
                break
            i += 1
    if has_double and always_inc:
        return True
    return False


valid_count = 0
valid_count2 = 0
for x in range(lower_bound, upper_bound+1):
    if valid_pass(str(x)):
        valid_count += 1
    if valid_pass2(str(x)):
        valid_count2 += 1
print(valid_count)
print(valid_count2)
