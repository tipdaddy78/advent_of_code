from hashlib import md5

# NO FILE INPUT, JUST STRING BELOW

searching = True
password = ""
cur = 0
start = "ffykfhsq"
# start = "abc" # Used for testing example on site.
#
# while searching:
#     hashed = md5((start + str(cur)).encode()).hexdigest()
#     if hashed[0:5] == "00000":
#         print("Found a match at index:", cur)
#         password += hashed[5]
#         if len(password) == 8:
#             searching = False
#     cur += 1
#
# print(password)
#
# # Resetting for part 2
# print("resetting for part 2....")
searching = True
cur = 0
newPassword = ['', '', '', '', '', '', '', '']

while searching:
    hashed = md5((start + str(cur)).encode()).hexdigest()
    if hashed[0:5] == "00000":
        print("Found a match at index:", cur, "- Relevant characters are:", hashed[0:7])
        if not hashed[5].isnumeric():
            cur += 1
            continue
        index = int(hashed[5])
        new_char = hashed[6]
        if index > 7:
            cur += 1
            continue
        else:
            if newPassword[index] == '':
                newPassword[index] = new_char
        if '' not in newPassword:
            searching = False
    cur += 1
print(newPassword)
