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
    if all(
        (el in pp.keys()) for el in ["byr", "iyr", "eyr", "hcl", "ecl", "pid", "hgt"]
    ):
        has_fields_passports.append(pp)


validations = {
    "byr": lambda x: x.isdigit() and 1920 <= int(x) <= 2002 and len(x) == 4,
    "iyr": lambda x: x.isdigit() and 2010 <= int(x) <= 2020 and len(x) == 4,
    "eyr": lambda x: x.isdigit() and 2020 <= int(x) <= 2030 and len(x) == 4,
    "hgt": lambda x: re.compile("\d+in|\d+cm").match(x) and 150 <= int(x[:-2]) <= 193
    if "cm" in x
    else 59 <= int(x[:-2]) <= 76,
    "hcl": lambda x: isinstance(x, str)
    and len(x) == 7
    and re.compile("#[\da-f]{6}").match(x),
    "ecl": lambda x: isinstance(x, str)
    and x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda x: x.isdigit() and len(x) == 9,
}

valid_passports = []

for pp in has_fields_passports:
    if all(validations.get(k, lambda x: True)(v) for (k, v) in pp.items()) == True:
        valid_passports.append(pp)
    else:
        print(pp)


print(len(valid_passports))