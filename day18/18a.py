import re


def calc(expression):
    numbers = [int(i) for i in re.findall("\d+", expression)]
    tasks = re.findall("[+,*]", expression)
    result = numbers.pop(0)
    while numbers:
        curr_numb = numbers.pop(0)
        curr_op = tasks.pop(0)
        if curr_op == "+":
            result += curr_numb
        if curr_op == "*":
            result *= curr_numb
    return result


INNER_PAR = re.compile("(\([\d\s\+\*]+\))")


def run(lines):
    result = 0
    for line in lines:
        inner_pars = INNER_PAR.findall(line)
        while inner_pars:
            for par in inner_pars:
                line = line.replace(par, str(calc(par[1:-1])))
            inner_pars = INNER_PAR.findall(line)
        result += calc(line)

    return result


def main():
    with open("18.txt") as input:
        lines = [line.strip() for line in input.readlines()]
        print(run(lines))

    return 0


if __name__ == "__main__":
    exit(main())