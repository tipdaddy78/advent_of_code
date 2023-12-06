import sys

from util.FileHelper import read_file_multiple_lines

lines = read_file_multiple_lines('2023', 'day5')

seed_to_soil = dict()
soil_to_fertilizer = dict()
fertilizer_to_water = dict()
water_to_light = dict()
light_to_temperature = dict()
temperature_to_humidity = dict()
humidity_to_location = dict()

# How parser will get correct map to put things in.
keys_to_converter = {
    "seed-to-soil": seed_to_soil,
    "soil-to-fertilizer": soil_to_fertilizer,
    "fertilizer-to-water": fertilizer_to_water,
    "water-to-light": water_to_light,
    "light-to-temperature": light_to_temperature,
    "temperature-to-humidity": temperature_to_humidity,
    "humidity-to-location": humidity_to_location
}


# Puts in the information needed to get the destination value out of the respective dictionary.
# Example line would be "50 98 2".
# This represents starting that source values of 50 and 51 (length 2) correspond to destination values of 98 and 99.
# The value of the map will be what number should be added to get the destination value.
def fill_conversion_map(converter_map, destination_start, source_start, length):
    key = (source_start, source_start + length - 1)
    value = destination_start - source_start
    converter_map[key] = value


def parse_input():
    current_map = seed_to_soil
    for line in lines:
        # First line only
        if line.startswith("seeds:"):
            seeds = list(line.split(":")[1].strip().split(" "))

        # Moving to next set of mappings
        elif line == '\n':
            current_map = None

        # time to get the map to fill in
        elif "map:" in line:
            key = line.split(" ")[0].strip()
            current_map = keys_to_converter[key]

        # Remaining lines are all three numbers separated by spaces.
        else:
            values = line.strip().split(" ")
            fill_conversion_map(current_map, int(values[0]), int(values[1]), int(values[2]))

    return seeds


def get_mapped_value(converter_map, source_val):
    for key in converter_map.keys():
        if key[0] <= source_val <= key[1]:
            return source_val + converter_map[key]

    return source_val


def map_ranges(converter_map, tuple_list):
    ret_tuple_list = list()
    while len(tuple_list) != 0:
        (tup_min, tup_max) = tuple_list.pop(0)
        found_match = False
        for key_min, key_max in converter_map.keys():
            if found_match:
                break

            # Range has no intersection, so move to next key
            if key_min > tup_max or key_max < tup_min:
                continue

            # Range to convert is entirely contained
            elif key_min <= tup_min and tup_max <= key_max:
                new_min = get_mapped_value(converter_map, tup_min)
                new_max = get_mapped_value(converter_map, tup_max)
                ret_tuple_list.append((new_min, new_max))
                found_match = True

            # Range is cut-off partially.  Convert the portion you can, and add portion you can't to the tuple list.
            else:
                # Lower bound is contained, but upper isn't.
                if key_min <= tup_min and tup_max > key_max:
                    new_min = get_mapped_value(converter_map, tup_min)
                    new_max = get_mapped_value(converter_map, key_max)
                    ret_tuple_list.append((new_min, new_max))
                    tuple_list.append((key_max + 1, tup_max))
                    found_match = True

                # Upper bound is contained, but lower isn't.
                else:
                    new_min = get_mapped_value(converter_map, key_min)
                    new_max = get_mapped_value(converter_map, tup_max)
                    ret_tuple_list.append((new_min, new_max))
                    tuple_list.append((tup_min, key_min - 1))
                    found_match = True

        # Final case, no key maps, so all continue on.
        if not found_match:
            ret_tuple_list.append((tup_min, tup_max))

    return ret_tuple_list


seeds = parse_input()

locations = list()
for seed in seeds:
    soil = get_mapped_value(seed_to_soil, int(seed))
    fertilizer = get_mapped_value(soil_to_fertilizer, soil)
    water = get_mapped_value(fertilizer_to_water, fertilizer)
    light = get_mapped_value(water_to_light, water)
    temperature = get_mapped_value(light_to_temperature, light)
    humidity = get_mapped_value(temperature_to_humidity, temperature)
    location = get_mapped_value(humidity_to_location, humidity)
    locations.append(location)

print(min(locations))

# Part 2, consider seeds in pairs of ranges
# Need to consider the range that will all be shifted in the same way.
i = 0
location_ranges = list()
while i < len(seeds):
    seed_start = int(seeds[i])
    seed_length = int(seeds[i+1])
    seed_tuples = list()
    seed_tuples.append((seed_start, seed_start + seed_length - 1))
    soil_tuples = map_ranges(seed_to_soil, seed_tuples)
    fertilizer_tuples = map_ranges(soil_to_fertilizer, soil_tuples)
    water_tuples = map_ranges(fertilizer_to_water, fertilizer_tuples)
    light_tuples = map_ranges(water_to_light, water_tuples)
    temperature_tuples = map_ranges(light_to_temperature, light_tuples)
    humidity_tuples = map_ranges(temperature_to_humidity, temperature_tuples)
    location_tuples = map_ranges(humidity_to_location, humidity_tuples)
    location_ranges.extend(location_tuples)

    i += 2

min_location = sys.maxsize
for location_range in location_ranges:
    if location_range[0] < min_location:
        min_location = location_range[0]
print(min_location)
