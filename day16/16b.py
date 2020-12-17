import re


def get_nearby_tickets(lines):
    heading_idx = lines.index("nearby tickets:\n")

    return lines[heading_idx + 1 :]


def get_your_ticket(lines):
    heading_idx = lines.index("your ticket:\n")

    return lines[heading_idx + 1]


def validate_ticket(all_numbers, ticket):
    for i in ticket.strip().split(","):
        if int(i) not in all_numbers:
            return False

    return True


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


def get_valid_tickets(valid_numbers, nearby_tickets):
    valid_tickets = []
    for ticket in nearby_tickets:
        if validate_ticket(valid_numbers, ticket):
            valid_tickets.append([int(i) for i in ticket.strip().split(",")])

    return valid_tickets


def get_row_rule_mapping(valid_tickets, rules_ranges):
    # row_rule = {i: [] for i in range(len(valid_tickets[0]))}
    row_rule = {}
    for v_ticket in valid_tickets:
        for idx, numb in enumerate(v_ticket):
            for rule in rules_ranges:
                if numb in rules_ranges[rule]:
                    row_rule.setdefault(idx, []).append(rule)

    results = {}
    for numb in row_rule:
        for rule in set(row_rule[numb]):
            rule_occurence = row_rule[numb].count(rule)
            results[numb] = [
                rule
                for rule in set(row_rule[numb])
                if rule_occurence == len(valid_tickets)
            ]
            """ if row_rule[numb].count(rule) == len(valid_tickets):
                results.setdefault(numb, []).append(rule) """
    # new_result = {i: results[i] for i in sorted(results, key=lambda x: len(results[x]))}
    return sorted(results, key=lambda x: len(row_rule[x]))
    """ new_result = {
        i: results[i] for i in sorted(results, key=lambda x: len(results[x]))
    } """


def get_valid_numbers_and_rule_ranges(lines):
    valid_numbers = []
    rule_ranges = {}

    for line in lines:
        ranges = re.findall("(\d+-\d+)", line)

        if ranges:
            rule = line.split(":")[0]
            rule_numbers = []
            for r in ranges:
                left_delimiter, right_delimiter = [int(i) for i in r.split("-")]
                valid_numbers += list(range(left_delimiter, right_delimiter + 1))
                rule_ranges.setdefault(rule, [])
                rule_ranges[rule] += list(range(left_delimiter, right_delimiter + 1))

        else:
            break

    return valid_numbers, rule_ranges


def main():
    with open("16.txt") as input:
        lines = input.readlines()
        valid_numbers = get_valid_numbers(lines)
        nearby_tickets = get_nearby_tickets(lines)
        your_ticket = get_your_ticket(lines)
        valid_numbers, rule_ranges = get_valid_numbers_and_rule_ranges(lines)
        valid_tickets = get_valid_tickets(valid_numbers, nearby_tickets)
        get_row_rule_mapping(valid_tickets, rule_ranges)


def main2():
    with open("16.txt") as input:
        all_numbers = []
        rule_numbers = []
        ticket_numbers = []
        invalid = []
        valid_tickets = []
        lines = input.readlines()
        rules_ranges = {}
        row_rule = {}
        my_ticket = []

        for idx, line in enumerate(lines):
            if line.strip() == "nearby tickets:":
                ticket_number_lines = lines[idx + 1 :]
                break
            elif line.strip() == "your ticket":
                my_ticket = lines[idx + 1 :]
            else:
                rules = re.findall("(\d+-\d+)", line)
                if rules:
                    req = line.split(":")[0]
                    for rule in rules:
                        numbers = [int(i) for i in rule.split("-")]
                        all_numbers += list(range(numbers[0], numbers[1] + 1))
                        rule_numbers += list(range(numbers[0], numbers[1] + 1))
                    rules_ranges[req] = rule_numbers
                    rule_numbers = []

        for ticket in ticket_number_lines:
            if validate_ticket(all_numbers, ticket):
                valid_tickets.append([int(i) for i in ticket.strip().split(",")])

        row_rule = {i: [] for i in range(len(valid_tickets[0]))}
        for v_ticket in valid_tickets:
            for idx, numb in enumerate(v_ticket):
                for rule in rules_ranges:
                    if numb in rules_ranges[rule]:
                        row_rule[idx].append(rule)

        results = {}
        for numb in row_rule:
            for req in set(row_rule[numb]):
                if row_rule[numb].count(req) == len(valid_tickets):
                    results.setdefault(numb, []).append(req)

        new_result = {
            i: results[i] for i in sorted(results, key=lambda x: len(results[x]))
        }

        has = []
        # print(new_result[10])
        print(sorted(results, key=lambda x: len(results[x])))
        print(new_result)
        for r in new_result:
            for req in new_result[r]:
                if req in has:
                    new_result[r] = [f for f in new_result[r] if f not in has]
                else:
                    has.append(req)
                    print("has")
                    print(has)

        print(new_result)

        """ for rule in rules_ranges:
            rules_ranges_cp = rules_ranges.copy()
            del rules_ranges_cp[rule]
            other_numbers = reduce(
                lambda acc, r: [*acc, *rules_ranges_cp[r]], rules_ranges_cp, []
            )
            new_rules_ranges[rule] = [
                i for i in rules_ranges[rule] if i not in other_numbers
            ] """

        # print(all_numbers)

        # print(run(numbers))
    my_ticket = [
        89,
        179,
        173,
        167,
        157,
        127,
        163,
        113,
        137,
        109,
        151,
        131,
        97,
        149,
        107,
        83,
        79,
        139,
        59,
        53,
    ]

    res = 1
    for i in [11, 7, 9, 0, 3, 4]:
        res *= my_ticket[i]

    print(res)

    return 0


if __name__ == "__main__":
    exit(main())