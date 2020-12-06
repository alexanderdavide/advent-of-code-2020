import math

results = []

with open("5.txt") as input:
    for line in input.readlines():
        row = {'directions': line[0:7], 'find': [0, 127]}
        column = {'directions': line[7:], 'find': [0, 7]}
        for axis in [row, column]:
            for direc in axis['directions']:
                if direc == 'F' or direc == 'L':
                    axis['find'][1] = axis['find'][0] + math.floor((axis['find'][1] - axis['find'][0]) / 2)
                else:
                    axis['find'][0] = axis['find'][0] + math.ceil((axis['find'][1] - axis['find'][0]) / 2)

        results.append(row['find'][0]*8+column['find'][0])

print([x for x in range(min(results), max(results)+1) if x not in results])

    