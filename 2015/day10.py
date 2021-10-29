def apply_look_say_iter(string):
    ret = ''
    cur = string[0]
    count = 1
    for i in range(len(string) - 1):
        next = string[i+1]
        if next == cur:
            count += 1
        else:
            ret += str(count) + cur
            count = 1
        cur = next
    ret += str(count) + cur
    return ret


s = "1113222113"
for x in range(40):
    s = apply_look_say_iter(s)

print(len(s))

# Part 2
s = "1113222113"
for x in range(50):
    s = apply_look_say_iter(s)

print(len(s))
