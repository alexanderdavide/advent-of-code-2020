from itertools import product
from functools import reduce
import re


def conv_dec_to_36bit(numb):
    result = "{0:b}".format(numb)

    while len(result) < 36:
        result = "0" + result

    return result


def conv_bit_to_dec(bit_iterable):
    return int("".join(bit_iterable), 2)


def transform_value(mask, numb):
    numb_as_list = list(numb)
    todo = [(idx, int(i)) for idx, i in enumerate(mask) if i != "X"]

    for do in todo:
        numb_as_list[do[0]] = str(do[1])

    return conv_bit_to_dec(numb_as_list)


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
                        mem[inst[0]] = transform_value(mask, conv_dec_to_36bit(inst[1]))
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