from util.FileHelper import read_file_multiple_lines


# Goes from 0 until it finds the first instance of winning,
# Once it finds that, it can know how many other things will also work
# This is found by taking the time value, subtracting i, and then finding the difference between that number and i
# But zero is also included, so have to add 1
def find_ways_above_record(time, record):
    i = 0
    while True:
        distance = i * (time - i)
        if distance > record:
            break
        i += 1

    return (time - i) - i + 1


lines = read_file_multiple_lines('2023', 'day6')

times = lines[0].strip().split(' ')
distances = lines[1].strip().split(' ')

# Remove blanks and first record, then convert to ints.
times = list(filter(bool, times))
times.pop(0)
times = list(map(int, times))
distances = list(filter(bool, distances))
distances.pop(0)
distances = list(map(int, distances))


product = 1
for n in range(len(times)):
    product *= find_ways_above_record(times[n], distances[n])

print(product)

# just grabbing the values from text file
print(find_ways_above_record(58996469, 478223210191071))
