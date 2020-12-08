import re


def count_bags_containing_shiny_gold_bag(lines):
    bags_count = 0

    for line in lines:
        color = " ".join(line.split(" ")[0:2])
        if color == "shiny_gold":
            continue
        elif find_shiny_gold(color, lines):
            bags_count += 1

    return bags_count


def find_shiny_gold(color, lines):
    line = [i for i in lines if i.startswith(color)][0]
    contents = re.findall("(\w+\s\w+)\sbag", line.split("contain", 1)[1])

    if "shiny gold" in contents:
        return True
    elif "no other" in contents:
        return False

    for color in contents:
        if find_shiny_gold(color, lines):
            return True

    return False


def main():
    with open("7.txt") as input:
        lines = input.readlines()

    print(count_bags_containing_shiny_gold_bag(lines))
    return 0


if __name__ == "__main__":
    exit(main())