from util.FileHelper import read_file_multiple_lines
from collections import Counter

lines = read_file_multiple_lines('2023', 'day7')
POINT_VALUE = 15

card_values = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
}


# Returns the "score" of the card
# Raises POINT_VALUE to the power of how many of cards there are
# X of a kind is POINT_VALUE ** X
# Full Houses end up as POINT_VALUE ** 2 + POINT_VALUE ** 3
# If all individual cards, returns the highest card by value in card_values
def score_hand(hand):
    counts = Counter(hand)
    score = 0
    # Useful for when it's 5 random cards
    highest = max(counts.values())

    # Determine high card
    if highest == 1:
        score = max(map(lambda x: card_values[x], hand))

    else:
        for count in counts.values():
            if count == 1:
                score += 1
            else:
                score += POINT_VALUE ** count

    return score


hands = list()
for line in lines:
    hand_and_bid = line.strip().split(' ')
    hand_score = score_hand(hand_and_bid[0])
    hand_values = list(map(lambda x: card_values[x], hand_and_bid[0]))
    hands.append((hand_score, hand_values, hand_and_bid[0], hand_and_bid[1]))

# It will sort by the score first, then it will look at the list of values.
# This SHOULD get everything into the proper order.
hands.sort()

winnings = 0
for i in range(len(hands)):
    hand = hands[i]
    print(hand)
    winnings += (i + 1) * int(hand[3])

print(winnings)
