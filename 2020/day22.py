game_results = dict()

class Deck:
    def __init__(self, cards=list()):
        self.starting = cards.copy()
        self.cards = cards

    def draw_card(self):
        return self.cards.pop(0)

    def add_cards(self, winner, loser):
        self.cards.append(winner)
        self.cards.append(loser)

    def get_score(self):
        l = len(self.cards)
        score = 0
        for c in self.cards:
            score += (l * c)
            l -= 1
        return score


class WarGame:
    def __init__(self, p1_cards, p2_cards):
        self.p1 = Deck(p1_cards)
        self.p2 = Deck(p2_cards)
        self.mem = dict()
        self.round = 0

    def play_game(self, m = 1):
        # first check to see if game has been "played" before.
        key = self.generate_key()
        if key in game_results.keys():
            # if it has, don't bother playing game, just return result
            return game_results.get(key)
        while len(self.p1.cards) != 0 and len(self.p2.cards) != 0:
            if m == 2:
                # Recursive mode games end if they've seen a state before.
                if not self.add_to_mem():
                    # in a state that's been seen,
                    # P1 wins.
                    key = self.generate_key()
                    score = self.p1.get_score()
                    game_results[key] = (1, score)
                    return (1, score)
            # Draw Cards
            c1 = self.p1.draw_card()
            c2 = self.p2.draw_card()
            # recursive mode initiates based on card values / deck lengths
            if m == 2 and len(self.p1.cards) >= c1 and len(self.p2.cards) >= c2:
                # sub-game needs to be played
                sub_p1 = self.p1.cards[:c1].copy()
                sub_p2 = self.p2.cards[:c2].copy()
                wg = WarGame(sub_p1, sub_p2)
                ret = wg.play_game(2)
                if ret[0] == 1:
                    # player 1 won the sub-game
                    self.p1.add_cards(c1, c2)
                else:
                    # player 2 won the sub-game
                    self.p2.add_cards(c2, c1)
            # No recursive, just use card value to determine winner.
            elif c1 > c2:
                self.p1.add_cards(c1, c2)
            else:
                self.p2.add_cards(c2, c1)
        # Based on the winner of the game, place the result in game results dict
        # This speeds things up for further rounds.
        if len(self.p1.cards) == 0:
            key = self.generate_key()
            score = self.p2.get_score()
            game_results[key] = (2, score)
            return (2, score)
        else:
            key = self.generate_key()
            score = self.p1.get_score()
            game_results[key] = (1, score)
            return (1, score)

    # Checks if state has been seen before
    # Returns True if state never seen and added
    # Returns False if state has been seen before.
    def add_to_mem(self):
        temp = list()
        temp.append('P1')
        for c1 in self.p1.cards:
            temp.append(str(c1))
        temp.append('P2')
        for c2 in self.p2.cards:
            temp.append(str(c2))
        if temp in self.mem.values():
            return False
        else:
            self.mem[self.round] = temp
            self.round += 1
            return True

    def generate_key(self):
        key = 'P1:'
        for c1 in self.p1.starting:
            key += str(c1)
            key += ','
        key += ' P2:'
        for c2 in self.p2.starting:
            key += str(c2)
            key += ','
        return key


def create_game():
    p1_cards = list()
    p2_cards = list()
    with open('day22.txt', 'r') as f:
        p1_done = False
        for line in f.readlines():
            if line.strip().isnumeric():
                if not p1_done:
                    p1_cards.append(int(line.strip()))
                else:
                    p2_cards.append(int(line.strip()))
            elif "Player 2" in line:
                p1_done = True
        f.close()
    wg = WarGame(p1_cards, p2_cards)
    return wg

def run(m):
    global game_results
    game_results = dict()
    wg = create_game()
    ret = wg.play_game(m)
    game_results.clear()
    return ret

print(run(1))
print(run(2))


