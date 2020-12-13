from functools import reduce


def run(arrival, buses):
    buses_times = {int(i): int(i) for i in buses.strip().split(",") if i != "x"}
    print(arrival)
    print(buses_times)
    greater = []
    while not greater:
        for time in buses_times:
            new_time = buses_times[time] + time
            buses_times[time] = new_time
            if new_time >= arrival:
                greater.append((time, time * (buses_times[time] - arrival)))
    print(greater)
    return


def main():
    with open("13.txt") as input:
        lines = input.readlines()
        arrival = int(lines[0].strip())
        buses = lines[1]
        # lines = reduce(lambda acc, el: [*acc, el.rstrip("\n")], lines, [])
        print(run(arrival, buses))

    return 0


if __name__ == "__main__":
    exit(main())