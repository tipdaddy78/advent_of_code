from util.FileHelper import read_file_multiple_lines

color_maxes = {
    "red": 12,
    "green": 13,
    "blue": 14
}
games = read_file_multiple_lines('2023', 'day2')

id_sum = 0
power_sum = 0
# Example game: "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
for game in games:
    game_to_rounds = game.strip().split(":")
    game_id = int(game_to_rounds[0].strip().split(' ')[1])
    invalid = False
    power = 1

    color_mins = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    rounds = game_to_rounds[1].strip().split(";")
    for game_round in rounds:
        amounts_and_colors = game_round.strip().split(",")
        for amount_and_color in amounts_and_colors:
            str_amount, color = amount_and_color.strip().split(" ")
            amount = int(str_amount.strip())
            if amount > color_maxes[color.strip()]:
                invalid = True
            if color_mins[color] < amount:
                color_mins[color] = amount
    if not invalid:
        id_sum += game_id

    for color_min in color_mins.values():
        power *= color_min
    power_sum += power

print(id_sum)
print(power_sum)