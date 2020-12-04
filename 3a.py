trees = 0

with open("3.txt") as input:
    idx = 0
    rows = input.readlines()
    for line in rows[1:]:
        line = line.strip("\n") * len(rows)
        idx += 3
        if line[idx] == "#":
            trees += 1

print(trees)
