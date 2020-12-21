lines = list()
nbr_valid = 0

with open('day4.txt', 'r') as f:
    lines = f.readlines()
    f.close()

for line in lines:
    words = line.split(" ")
    words_tot = len(words)
    curr = list()
    for word in words:
        word_no_newline = word.replace("\n", "")
        sorted_word = ''.join(sorted(word_no_newline))
        if word not in curr and word_no_newline not in curr and sorted_word not in curr:
            curr.append(sorted_word)
    if len(curr) == len(words):
        nbr_valid += 1

print(nbr_valid)