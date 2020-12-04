import re

valid = 0

with open("2.txt") as input:
    for line in input.readlines():
        try:
            minOcc = int(re.search('(\d+)-', line).group(1))
            maxOcc = int(re.search('-(\d+)', line).group(1))
            char = re.search('([a-z]):', line).group(1)
            target = line.split(':')[1].strip()
            count = target.count(char)
            if count >= minOcc and count <= maxOcc:
                valid+=1
        except:
            print("error")
            raise

print(valid)        


    