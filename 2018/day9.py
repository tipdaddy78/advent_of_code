class marble:
    def __init__(self, value):
        self.next = self
        self.previous = self
        self.value = value

    def setNext(self, marble):
        self.next = marble

    def setPrevious(self, marble):
        self.previous = marble


data = list
with open('day9.txt', 'r') as f:
    data = f.read().strip().split(' ')
    f.close()

players = int(data[0])
last = int(data[6])*100
scores = dict()
for i in range(players):
    scores[i] = 0

cur_p = 0
cur_m = marble(0)
for i in range(1, last+1):
    if i % 23 == 0:
        cur_score = scores.get(cur_p)
        cur_score += i
        sevBack = cur_m.previous.previous.previous.previous.previous.previous.previous
        sevBack.previous.next = sevBack.next
        sevBack.next.previous = sevBack.previous
        cur_score += sevBack.value
        scores[cur_p] = cur_score
        cur_m = sevBack.next
    else:
        m = marble(i)
        oneAhead = cur_m.next
        twoAhead = cur_m.next.next
        m.previous = oneAhead
        m.next = twoAhead
        oneAhead.next = m
        twoAhead.previous = m
        cur_m = m

    cur_p  = (cur_p + 1) % players

print(max(scores.values()))
