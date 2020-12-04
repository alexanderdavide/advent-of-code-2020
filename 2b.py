import re

with open('2.txt') as input:
    valid = 0

    for line in input.readlines():
        try:
            firstPos = int(re.search('(\d+)-', line).group(1))
            secondPos = int(re.search('-(\d+)', line).group(1))
            char = re.search('([a-z]):', line).group(1)
            target = line.split(':')[-1].strip()
            if target[firstPos-1] == char and target[secondPos-1] == char:
                pass
            elif target[firstPos-1] == char or target[secondPos-1] == char:
                valid += 1
        except Exception as e:
            print(e)
            exit(-1)
    print(valid)

