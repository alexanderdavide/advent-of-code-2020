from itertools import product
from functools import reduce
import re


def conv_bit_to_dec(bit_iterable):
    return int("".join(bit_iterable), 2)


def conv_dec_to_36bit(numb):
    result = "{0:b}".format(numb)

    while len(result) < 36:
        result = "0" + result

    return result


def generate(length, chars="01"):
    return list(product(["0", "1"], repeat=length))


def transform_location(mask, loc):
    loc_as_list = list(loc)
    todo = [(idx, i) for idx, i in enumerate(mask) if i != "0"]
    locations = []

    x_idxs = []
    for do in todo:
        if str(do[1]) == "X":
            x_idxs.append(do[0])
        loc_as_list[do[0]] = str(do[1])

    options = list(generate(len(x_idxs)))
    for o in options:
        iter_o = iter(o)
        new_loc = loc_as_list.copy()
        for x in x_idxs:
            loc_as_list[x] = next(iter_o)
        locations.append(conv_bit_to_dec(loc_as_list))

    return locations


def main():
    with open("14.txt") as input:
        lines = input.readlines()
        instructions = []
        mask = "X" * 36
        mem = {}
        for idx, line in enumerate(lines):
            if line.startswith("mask") or idx == len(lines) - 1:
                if instructions:
                    for inst in instructions:
                        locations = transform_location(mask, conv_dec_to_36bit(inst[0]))
                        value = inst[1]
                        for loc in locations:
                            mem[loc] = value
                mask = line[7:].strip()
                instructions = []
            else:
                loc = int(re.search("\[(\d+)\]", line.strip()).group(1))
                value = int(line.split("= ")[1].strip())
                instructions.append((loc, value))

        print(reduce(lambda acc, x: acc + mem[x], mem, 0))
    return 0


if __name__ == "__main__":
    exit(main())