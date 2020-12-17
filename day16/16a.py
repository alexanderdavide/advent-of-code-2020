import re


def validate_ticket(all_numbers, ticket):
    for i in ticket.strip().split(","):
        if int(i) not in all_numbers:
            return False
    return True


def get_nearby_tickets(lines):
    heading_idx = lines.index("nearby tickets:\n")

    return lines[heading_idx + 1 :]


def calc_error_rate(valid_numbers, nearby_tickets):
    error_rate = 0

    for ticket in nearby_tickets:
        for numb in [int(i) for i in ticket.strip().split(",")]:
            if numb not in valid_numbers:
                error_rate += numb

    return error_rate


def get_valid_numbers(lines):
    valid_numbers = []

    for line in lines:
        ranges = re.findall("(\d+-\d+)", line)

        if ranges:
            rule = line.split(":")[0]
            for r in ranges:
                left_delimiter, right_delimiter = [int(i) for i in r.split("-")]
                valid_numbers += list(range(left_delimiter, right_delimiter + 1))
        else:
            break

    return valid_numbers


def main():
    with open("16.txt") as input:
        lines = input.readlines()
        valid_numbers = get_valid_numbers(lines)
        nearby_tickets = get_nearby_tickets(lines)
        print(calc_error_rate(valid_numbers, nearby_tickets))

    return 0


if __name__ == "__main__":
    exit(main())