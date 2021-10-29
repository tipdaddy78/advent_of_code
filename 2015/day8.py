from util.FileHelper import read_file_multiple_lines

lines = read_file_multiple_lines('2015', 'day8')

x = "aaa\"aaa"
y = x.encode()

literal_count = 0
mem_count = 0
encoded_count = 0
for line in lines:
    # remove outer quotes and count them
    l = line[1:-1]
    mem_count += 2
    encoded_count += 6

    i = 0
    while i < len(l):
        next = ''
        if i < len(l) - 1:
            next = l[i+ 1]
        cur = l[i]
        if cur == "\\":
            if next == 'x':
                encoded_count += 5
                mem_count += 4
                i += 4
            else:
                encoded_count += 4
                mem_count += 2
                i += 2
            literal_count += 1
        else:
            encoded_count += 1
            mem_count += 1
            literal_count += 1
            i += 1

print(mem_count - literal_count)
print(encoded_count - mem_count)


