from functools import reduce

input = None
with open("3.txt") as input:
    input = input.readlines()

trees_per_slope = []

for slope in [1, 3, 5, 7]:
    idx = 0
    trees = 0
    for line in input[1:]:
        line = line.strip("\n") * len(input)
        idx += slope
        if line[idx] == "#":
            trees += 1
    trees_per_slope.append(trees)

idx = 0
trees = 0
for line in input[2::2]:
    line = line.strip("\n") * len(input[2::2])
    idx += 1
    if line[idx] == "#":
        trees += 1
trees_per_slope.append(trees)

print(reduce(lambda x, y: x * y, trees_per_slope))
