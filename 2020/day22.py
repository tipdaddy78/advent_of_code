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

    def get_score(self, p1):
        l = len(self.cards)
        score = 0
        for c in self.cards:
            score += (l * c)
            l -= 1
        if p1:
            score *= -1
        return score


class WarGame:
    def __init__(self, p1_cards, p2_cards):
        self.p1 = Deck(p1_cards)
        self.p2 = Deck(p2_cards)
        self.mem = set()
        self.round = 0

    def play_game(self, m = 1):
        # first check to see if game has been "played" before.
        key = self.generate_key(True)
        if key in game_results.keys():
            # if it has, don't bother playing game, just return result
            return game_results.get(key)
        while len(self.p1.cards) != 0 and len(self.p2.cards) != 0:
            if m == 2:
                # Recursive mode games end if they've seen a state before.
                if not self.add_to_mem():
                    # in a state that's been seen,
                    # P1 wins.
                    key = self.generate_key(True)
                    score = self.p1.get_score(True)
                    game_results[key] = score
                    return score
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
                if ret < 0: # Scores are negative when P1 wins.
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
            key = self.generate_key(True)
            score = self.p2.get_score(False)
            game_results[key] = score
            return score
        else:
            key = self.generate_key(True)
            score = self.p1.get_score(True)
            game_results[key] = score
            return score

    # Checks if state has been seen before
    # Returns True if state never seen and added
    # Returns False if state has been seen before.
    def add_to_mem(self):
        key = self.generate_key(False)
        if key in self.mem:
            return False
        else:
            self.mem.add(key)
            return True

    def generate_key(self, game):
        deck1 = list()
        deck2 = list()
        if game:
            deck1 = self.p1.starting
            deck2 = self.p2.starting
        else:
            deck1 = self.p1.cards
            deck2 = self.p2.cards
        key = 'P1:'
        key += str(deck1)
        key += ' P2:'
        key += str(deck2)
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

# print(run(1))
print(run(2))


