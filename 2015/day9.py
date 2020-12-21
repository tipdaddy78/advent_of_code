distances = dict()
locations = list()


with open('day9.txt', 'r') as f:
    lines = f.readlines()
    f.close()

for line in lines:
    line = line.replace('\n', '')
    parts = line.split('=')
    word_parts = parts[0].split("to")
    word_duple = word_parts[0].strip(), word_parts[1].strip()
    word_duple2 = word_parts[1].strip(), word_parts[0].strip()
    distances[word_duple] = int(parts[1].strip())
    distances[word_duple2] = int(parts[1].strip())
    if word_parts[0].strip() not in locations:
        locations.append(word_parts[0].strip())

amounts = list()
checked = list()
for direction1 in distances.keys():
    if direction1 not in checked:
        visited = list()
        distance = 0
        start1 = direction1[0]
        end1 = direction1[1]
        visited.append(start1)
        if end1 not in visited:
            visited.append(end1)
            distance += distances[direction1]
            cur_distance1 = distance
            for direction2 in distances.keys():
                distance = cur_distance1
                start2 = direction2[0]
                end2 = direction2[1]
                if end1 == start2 and end2 not in visited:
                    visited.append(end2)
                    distance += distances[direction1]
                    cur_distance2 = distance
                    for direction3 in distances.keys():
                        distance = cur_distance2
                        start3 = direction3[0]
                        end3 = direction3[1]
                        if end2 == start3 and end3 not in visited:
                            visited.append(end3)
                            distance += distances[direction3]
                            cur_distance3 = distance
                            for direction4 in distances.keys():
                                distance = cur_distance3
                                start4 = direction4[0]
                                end4 = direction4[1]
                                if end3 == start4 and end4 not in visited:
                                    visited.append(end4)
                                    distance += distances[direction4]
                                    cur_distance4 = distance
                                    for direction5 in distances.keys():
                                        distance = cur_distance4
                                        start5 = direction5[0]
                                        end5 = direction5[1]
                                        if end4 == start5 and end5 not in visited:
                                            visited.append(end5)
                                            distance += distances[direction5]
                                            cur_distance5 = distance
                                            for direction6 in distances.keys():
                                                distance = cur_distance5
                                                start6 = direction6[0]
                                                end6 = direction6[1]
                                                if end5 == start6 and end6 not in visited:
                                                    visited.append(end6)
                                                    distance += distances[direction6]
                                                    cur_distance6 = distance
                                                    for direction7 in distances.keys():
                                                        distance = cur_distance6
                                                        start7 = direction7[0]
                                                        end7 = direction7[1]
                                                        if end6 == start7 and end7 not in visited:
                                                            distance += distances[direction7]
                                                            amounts.append(distance)
                                                            break
                                                    visited.pop()
                                            visited.pop()
                                    visited.pop()
                            visited.pop()
                    visited.pop()
            visited.pop()
    visited.pop()
    checked.append(direction1)


print(min(amounts))

