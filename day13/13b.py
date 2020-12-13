import math
from functools import reduce


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def run(buses_offset_loop):
    time = 0
    current_bus = buses_offset_loop.pop(0)
    step = current_bus[1]

    while True:
        offset = current_bus[0]
        loop = current_bus[1]
        if (time + offset) % loop == 0:
            step = lcm(loop, step)
            if buses_offset_loop:
                current_bus = buses_offset_loop.pop(0)
            else:
                break
        else:
            time += step

    return time


def main():
    with open("13.txt") as input:
        lines = input.readline().strip().split(",")
        buses_offset_loop = [(idx, int(i)) for idx, i in enumerate(lines) if i != "x"]
        print(run(buses_offset_loop))

    return 0


if __name__ == "__main__":
    exit(main())