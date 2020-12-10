from functools import reduce


PREAMBEL = 25


def get_possible_sums(numbers):
    sums = []
    for idx, numb in enumerate(numbers[:-1]):
        for addend in numbers[idx + 1 :]:
            if numb != addend:
                sums.append(numb + addend)
    return sums


def find_invalid_number(numbers):
    for idx, numb in enumerate(numbers[PREAMBEL:]):
        if numb in get_possible_sums(numbers[idx : PREAMBEL + idx]):
            continue
        else:
            return numb


def main():
    with open("9.txt") as input:
        lines = input.readlines()
        numbers = reduce(lambda acc, el: [*acc, int(el.rstrip("\n"))], lines, [])
        print(find_invalid_number(numbers))
    return 0


if __name__ == "__main__":
    exit(main())