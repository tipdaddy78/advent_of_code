from collections import deque
from util.FileHelper import read_file_multiple_lines

illegal_scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
legal_scores = {')': 1, ']': 2, '}': 3, '>': 4}
closer_to_opener = {')': '(', ']': '[', '}': '{', '>': '<'}
opener_to_closer = {'(': ')', '[': ']', '{': '}', '<': '>'}

data_lines = read_file_multiple_lines('2021', 'day10')
incomplete_lines = list()
incomplete_queues = dict()
error_score = 0
idx = 0
for data in data_lines:
    illegal = False
    q = deque()
    for d in data.strip():
        if d in ('(', '[', '{', '<'):
            q.append(d)
        else:
            opener = q.pop()
            # Found an illegal line
            if closer_to_opener[d] != opener:
                illegal = True
                error_score += illegal_scores[d]
                illegal = True
                break
    if not illegal:
        incomplete_lines.append(data.strip())
        incomplete_queues[idx] = q
        idx += 1

print(error_score)

# Part 2, complete incomplete lines.
incomplete_scores = list()
for i in range(len(incomplete_lines)):
    score = 0
    q = incomplete_queues[i]
    while len(q) > 0:
        opener = q.pop()
        closer = opener_to_closer[opener]
        score = (score * 5) + legal_scores[closer]
    incomplete_scores.append(score)

sorted_scores = sorted(incomplete_scores)
print(sorted_scores[int(len(incomplete_scores)/2)])



