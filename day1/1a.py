input = []

with open("1.txt") as fp:
    for line in fp:
        input.append(int(line[0:-1]))

for addend1 in input:
    for addend2 in list(filter(lambda x: x != addend1, input)):
        if addend1 + addend2 == 2020:
            print(f"{addend1} + {addend2}")
            print(addend1 * addend2)
            break
