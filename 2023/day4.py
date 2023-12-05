from util.FileHelper import read_file_multiple_lines

cards = read_file_multiple_lines('2023', 'day4')


def calculate_card_score(winning_set, card_set):
    matches = get_number_of_matches(winning_set, card_set)
    if matches == 0:
        return 0
    elif matches == 1:
        return 1
    else:
        return 2 ** (matches - 1)


def get_number_of_matches(winning_set, card_set):
    return len(winning_set.intersection(card_set))


def get_sets_from_card(card):
    card_parts = card.strip().split(":")
    winning_and_have = card_parts[1].strip().split("|")
    winning_set = set(filter(bool, winning_and_have[0].strip().split(" ")))
    card_set = set(filter(bool, winning_and_have[1].strip().split(" ")))
    return winning_set, card_set


card_dict = dict()
score = 0
# Example Card: "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
for index, card in enumerate(cards):
    card_dict[index + 1] = card
    winning_set, card_set = get_sets_from_card(card)
    score += calculate_card_score(winning_set, card_set)

print(score)

# Part 2, making copies and then processing those copies.
instances = dict()
for index in card_dict.keys():
    instances[index] = 1


# Process one card, and add the copies to the list.
for index in card_dict.keys():
    card = card_dict[index]
    winning_set, card_set = get_sets_from_card(card)
    matches = get_number_of_matches(winning_set, card_set)
    for x in range(instances[index]):
        for n in range(index + 1, index + 1 + matches):
            if n in card_dict.keys():
                instances[n] += 1

print(sum(instances.values()))
