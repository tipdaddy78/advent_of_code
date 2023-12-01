import sys

from util.FileHelper import read_file_multiple_lines

lines = read_file_multiple_lines('2023', 'day1')


def find_calibration_sum(file_lines):
    calibration_values = list()
    for line in file_lines:
        first_num = None
        last_num = None
        for char in line:
            if char.isnumeric():
                if first_num is None:
                    first_num = char
                last_num = char
        calibration_values.append(int(first_num + last_num))

    sum = 0
    for calibration_value in calibration_values:
        sum += calibration_value

    return sum


print(find_calibration_sum(lines))

# Relations of string representations of a number.
string_numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

# Replace all string representations of numbers, with the numbers themselves.
formatted_lines = list()
for line in lines:
    replacing = True
    current_formatted_line = line
    while replacing:
        best_key = ""
        best_key_index = sys.maxsize
        for key in string_numbers.keys():
            index = current_formatted_line.find(key)
            if index < best_key_index and index != -1:
                best_key = key
                best_key_index = index

        # No integer strings found, done replacing
        if best_key_index == sys.maxsize:
            replacing = False
            continue

        current_formatted_line = current_formatted_line.replace(best_key, string_numbers[best_key], 1)

    formatted_lines.append(current_formatted_line)

print(find_calibration_sum(formatted_lines))
