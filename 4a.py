import re

passports = []

with open("4.txt") as input:
    data = {}
    for line in input.readlines():
        if line == "\n":
            passports.append(data)
            data = {}
        else:
            for item in line.strip("\n").split(" "):
                data[item.split(":")[0]] = item.split(":")[1]
    passports.append(data)


has_fields_passports = []
for pp in passports:
    print(list(pp.keys()))
    if all(
        (el in pp.keys()) for el in ["byr", "iyr", "eyr", "hcl", "ecl", "pid", "hgt"]
    ):
        has_fields_passports.append(pp)

print(len(has_fields_passports))