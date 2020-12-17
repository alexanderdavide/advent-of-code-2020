def run(lines):
    act_cubes = set()

    for y, row in enumerate(lines):
        for x, char in enumerate(row):
            if char == "#":
                act_cubes.add((y, x, 0, 0))

    for cycle in range(6):
        new_act_cubes = act_cubes.copy()
        inact_cubes_w_act_nghbrs = {}
        for y, x, z, w in act_cubes:
            act_nghbrs_count = 0
            for y_change in [-1, 0, 1]:
                for x_change in [-1, 0, 1]:
                    for z_change in [-1, 0, 1]:
                        for w_change in [-1, 0, 1]:
                            if 0 == y_change == x_change == z_change == w_change:
                                continue
                            nghbr = (
                                y + y_change,
                                x + x_change,
                                z + z_change,
                                w + w_change,
                            )
                            if nghbr in act_cubes:
                                act_nghbrs_count += 1
                            else:
                                if nghbr not in inact_cubes_w_act_nghbrs:
                                    inact_cubes_w_act_nghbrs[nghbr] = 0
                                inact_cubes_w_act_nghbrs[nghbr] += 1
            if act_nghbrs_count not in [2, 3]:
                new_act_cubes.discard((y, x, z, w))
        for cube in inact_cubes_w_act_nghbrs:
            if inact_cubes_w_act_nghbrs[cube] == 3:
                new_act_cubes.add(cube)
        act_cubes = new_act_cubes

    return len(act_cubes)


def main():
    with open("17.txt") as input:
        lines = [line.strip() for line in input.readlines()]
        print(run(lines))

    return 0


if __name__ == "__main__":
    exit(main())