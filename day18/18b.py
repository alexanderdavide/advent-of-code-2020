import re
from operator import mul
from functools import reduce


INNER_PAR = re.compile("(\([\d\s\+\*]+\))")
PLUS_OP = re.compile("(\d+\s*\+\s*\d+)")


def calc(expression):
    plus_ops = PLUS_OP.findall(expression)
    while plus_ops:
        for p_op in plus_ops:
            expression = expression.replace(
                p_op, str(sum([int(i) for i in re.findall("\d+", p_op)])), 1
            )
        plus_ops = PLUS_OP.findall(expression)
    numbers = [int(i) for i in re.findall("\d+", expression)]
    return reduce(mul, numbers)


def run(lines):
    result = 0
    for line in lines:
        while INNER_PAR.findall(line):
            for par in INNER_PAR.findall(line):
                line = line.replace(par, str(calc(par[1:-1])))
        result += calc(line)

    return result


def main():
    with open("18.txt") as input:
        lines = [line.strip() for line in input.readlines()]
        print(run(lines))

    return 0


if __name__ == "__main__":
    exit(main())