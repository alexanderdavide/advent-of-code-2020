from functools import reduce
import importlib

nine_a = importlib.import_module("9a", package=None)


def find_encryption_weakness(numbers):
    invalid_number = nine_a.find_invalid_number(numbers)
    for idx, _ in enumerate(numbers):
        candidates = []
        for candidate in numbers[idx:]:
            candidates.append(candidate)
            if sum(candidates) == invalid_number:
                return min(candidates) + max(candidates)
            elif sum(candidates) > invalid_number:
                break


def main():
    with open("9.txt") as input:
        lines = input.readlines()
        numbers = reduce(lambda acc, el: [*acc, int(el.rstrip("\n"))], lines, [])
        print(find_encryption_weakness(numbers))
    return 0


if __name__ == "__main__":
    exit(main())