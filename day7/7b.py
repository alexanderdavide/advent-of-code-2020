import re


def build_color_contents(lines):
    color_contents = {}

    for line in lines:
        re_color_contains = re.compile("^(\w+\s\w+) bags contain (.*)$").match(line)
        contents = {
            color: int(amount)
            for amount, color in re.compile(r"(\d+) (\w+\s\w+) bag").findall(
                re_color_contains[2]
            )
        }
        color_contents[re_color_contains[1]] = contents

    return color_contents


def count_bags_inside_shiny_gold_bag(color_contents):
    bags_count = 0
    todo = [{"shiny gold": 1}]

    while todo:
        item = todo.pop()
        color = next(iter(item))
        amount = item[color]
        bags_count += amount
        for content_color in color_contents[color]:
            todo.append({content_color: amount * color_contents[color][content_color]})

    return bags_count - 1


def main():
    with open("7.txt") as input:
        lines = input.readlines()

    color_contents = build_color_contents(lines)
    print(count_bags_inside_shiny_gold_bag(color_contents))

    return 0


if __name__ == "__main__":
    exit(main())