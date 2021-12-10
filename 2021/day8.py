from util.FileHelper import read_file_multiple_lines

data = read_file_multiple_lines('2021', 'day8')

p1_lengths = [2, 3, 4, 7]

# Part 1, just counting 1's, 4's, 7's and 8's
p1_count = 0
for d in data:
    output_signals = d.strip().split('|')[1].strip().split(' ')
    for o in output_signals:
        if len(o) in p1_lengths:
            p1_count += 1

print(p1_count)


def get_shared_segment_count(unique, non):
    count = 0
    for u in unique:
        if u in non:
            count += 1
    return count


# Table of # of segments shared between numbers w/ unique # of segments to non-unique
#############################
#     0 | 2 | 3 | 5 | 6 | 9 #
# 1 | 2 | 1 | 1 | 1 | 1 | 2 #
# 4 | 3 | 2 | 3 | 3 | 3 | 4 #
# 7 | 3 | 2 | 3 | 2 | 2 | 3 #
# 8 | 6 | 5 | 5 | 5 | 6 | 6 #
#############################
output_count = 0
for d in data:
    nums = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    num_dict = dict()
    one = ''
    four = ''
    seven = ''
    eight = ''
    unidentified = set()
    codes = d.strip().split(' ')
    for code in codes:
        if '|' in code:
            continue
        sorted_code = "".join(sorted(code))
        match len(sorted_code):
            case 2:
                one = sorted_code
                num_dict[sorted_code] = '1'
                nums.discard('1')
            case 3:
                seven = sorted_code
                num_dict[sorted_code] = '7'
                nums.discard('7')
            case 4:
                four = sorted_code
                num_dict[sorted_code] = '4'
                nums.discard('4')
            case 7:
                eight = sorted_code
                num_dict[sorted_code] = '8'
                nums.discard('8')
            case _:
                unidentified.add(sorted_code)
    for u in unidentified:
        # Determine how many segments it shares with all other numbers.
        one_match = get_shared_segment_count(one, u)
        four_match = get_shared_segment_count(four, u)
        seven_match = get_shared_segment_count(seven, u)
        eight_match = get_shared_segment_count(eight, u)
        if one_match == 2 and four_match == 3 and seven_match == 3 and eight_match == 6:
            num_dict[u] = '0'
            nums.discard('0')
        elif one_match == 1 and four_match == 2 and seven_match == 2 and eight_match == 5:
            num_dict[u] = '2'
            nums.discard('2')
        elif one_match == 1 and four_match == 3 and seven_match == 3 and eight_match == 5:
            num_dict[u] = '3'
            nums.discard('3')
        elif one_match == 1 and four_match == 3 and seven_match == 2 and eight_match == 5:
            num_dict[u] = '5'
            nums.discard('5')
        elif one_match == 1 and four_match == 3 and seven_match == 2 and eight_match == 6:
            num_dict[u] = '6'
            nums.discard('6')
        elif one_match == 2 and four_match == 4 and seven_match == 3 and eight_match == 6:
            num_dict[u] = '9'
            nums.discard('9')
    output_signals = d.strip().split('|')[1].strip().split(' ')
    output_num = ''
    for o in output_signals:
        sort = "".join(sorted(o))
        num = num_dict.get(sort)
        if num:
            output_num += num_dict.get(sort)
        else:
            if len(nums) == 1:
                num_dict[sort] = nums.pop()
                output_num += num_dict.get(sort)
    output_count += int(output_num)

print(output_count)
