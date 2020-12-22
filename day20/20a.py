from operator import mul
from functools import reduce


def get_tiles_borders(lines):
    tiles_borders = {}  # {[t, r, b, l], ..}
    curr_tile_line = 0
    curr_tile_id = None

    for line in lines:
        if line.startswith("T"):
            curr_tile_id = line[5:-1]
            tiles_borders[curr_tile_id] = ["", "", "", ""]
        elif line == "":
            curr_tile_line = 0
            curr_tile_id = None
        else:
            if curr_tile_line == 0:
                tiles_borders[curr_tile_id][0] = line
                tiles_borders[curr_tile_id][1] += line[-1]
                tiles_borders[curr_tile_id][3] += line[0]
            elif curr_tile_line == 9:
                tiles_borders[curr_tile_id][2] = line
                tiles_borders[curr_tile_id][1] += line[-1]
                tiles_borders[curr_tile_id][3] += line[0]
            else:
                tiles_borders[curr_tile_id][1] += line[-1]
                tiles_borders[curr_tile_id][3] += line[0]
            curr_tile_line += 1

    return tiles_borders


def find_corners(tiles_borders):
    corner_ids = []
    border_variations = []

    for tile_id, borders in tiles_borders.items():
        border_variations += borders + [b[::-1] for b in borders]
    for tile_id, borders in tiles_borders.items():
        if sum([1 for b in borders if border_variations.count(b) == 1]) == 2:
            corner_ids.append(int(tile_id))

    return reduce(mul, corner_ids)


def main():
    with open("20.txt") as input:
        lines = [line.strip() for line in input.readlines()]
        tiles_borders = get_tiles_borders(lines)
        print(find_corners(tiles_borders))

    return 0


if __name__ == "__main__":
    exit(main())