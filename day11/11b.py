from functools import reduce


def index_exists(ls, i):
    try:
        t = ls[i]
        return True
    except IndexError:
        return False


def count_adjacent_occupied(rows, seat):
    count = 0

    todo = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]

    for change in todo:
        x = seat[0] + change[0]
        y = seat[1] + change[1]
        while index_exists(rows, y) and index_exists(rows[y], x):
            if x < 0 or y < 0:
                break
            elif rows[y][x] == "#":
                count += 1
                break
            elif rows[y][x] == "L":
                break
            else:
                x += change[0]
                y += change[1]
    return count


def run(rows, before=0):
    new_rows = []
    total = 0
    for idx_y, row in enumerate(rows):
        new_rows.append([])
        for idx_x, seat in enumerate(row):
            if count_adjacent_occupied(rows, (idx_x, idx_y)) == 0 and seat == "L":
                new_rows[idx_y].append("#")
                total += 1
            elif count_adjacent_occupied(rows, (idx_x, idx_y)) >= 5 and seat == "#":
                new_rows[idx_y].append("L")
            else:
                new_rows[idx_y].append(seat)
                if seat == "#":
                    total += 1
    if total == before:
        return total

    return run(new_rows, total)


def main():
    with open("11.txt") as input:
        lines = input.readlines()
        rows = reduce(lambda acc, el: [*acc, list(el.rstrip("\n"))], lines, [])
        print(run(rows))
    return 0


if __name__ == "__main__":
    exit(main())