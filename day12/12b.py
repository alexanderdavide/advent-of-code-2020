from functools import reduce


def make_deg_between_0_360(deg):
    if deg >= 360:
        return deg - 360
    elif deg < 0:
        return deg + 360

    return deg


def run(lines):
    facing_to_deg = {"N": 0, "E": 90, "S": 180, "W": 270}

    manhattan = {90: 0, 270: 0, 0: 0, 180: 0}
    waypoint = {90: 10, 0: 1, 270: 0, 180: 0}

    for line in lines:
        direc = line[0]
        change = int(line[1:])

        if direc == "F":
            for d in waypoint:
                manhattan[d] += change * waypoint[d]
        elif direc == "R":
            new_waypoint = {}
            for d in waypoint:
                new_deg = make_deg_between_0_360(d + change)
                new_waypoint[new_deg] = waypoint[d]
            waypoint = new_waypoint
        elif direc == "L":
            new_waypoint = {}
            for d in waypoint:
                new_deg = make_deg_between_0_360(d - change)
                new_waypoint[new_deg] = waypoint[d]
            waypoint = new_waypoint
        else:
            waypoint[facing_to_deg[direc]] += change

    return abs(manhattan[90] - manhattan[270]) + abs(manhattan[0] - manhattan[180])


def main():
    with open("12.txt") as input:
        lines = input.readlines()
        lines = reduce(lambda acc, el: [*acc, el.rstrip("\n")], lines, [])
        print(run(lines))
    return 0


if __name__ == "__main__":
    exit(main())