import re


def run(numbers):
    is_spoken = {i: [idx] for idx, i in enumerate(numbers)}

    i = len(is_spoken)
    while len(numbers) < 30000000:
        last_number = numbers[-1]

        if last_number in is_spoken:
            when = is_spoken[last_number]

            if len(when) > 1:
                diff = when[-1] - when[-2]
                numbers.append(diff)
                is_spoken.setdefault(diff, []).append(i)
            else:
                numbers.append(0)
                is_spoken.setdefault(0, []).append(i)

        i += 1

    return numbers[-1]


def main():
    with open("15.txt") as input:
        numbers = [int(i) for i in input.readline().strip().split(",")]
        print(run(numbers))

    return 0


if __name__ == "__main__":
    exit(main())