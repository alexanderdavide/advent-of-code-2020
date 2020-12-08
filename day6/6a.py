count = 0

with open("6.txt") as input:
    answers = []
    lines = input.readlines()
    for idx, line in enumerate(lines):
        if line == "\n":
            count += len(set(answers))
            answers = []
        else:
            answers += list(line.strip("\n"))
    count += len(set(answers))

print(count)