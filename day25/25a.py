def transform(subject, loop_size):
    calc = 1
    for _ in range(loop_size):
        calc *= subject
        calc = calc % 20201227

    return calc


def brute_force_loop_size(subject, nbr):
    loop_size = 0
    calc = 1
    while calc != nbr:
        calc *= subject
        calc = calc % 20201227
        loop_size += 1

    return loop_size


def main():
    with open("25.txt") as input:
        lines = [int(i) for i in input.readlines()]
        pk1, pk2 = lines
        loop_size_1 = brute_force_loop_size(7, pk2)
        print(transform(pk1, loop_size_1))
    return 0


if __name__ == "__main__":
    exit(main())