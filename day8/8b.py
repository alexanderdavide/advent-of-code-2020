def terminates_successfully_and_accumulates(lines):
    lines_run_by_idx = []
    idx = 0
    acc = 0

    while -1 < idx < len(lines):
        if idx in lines_run_by_idx:
            return (False, acc)
        else:
            lines_run_by_idx.append(idx)
            instruction = lines[idx][0:3]
            number = lines[idx].split()[1].strip("\n")
            if instruction == "nop":
                idx += 1
                continue
            elif instruction == "jmp":
                if "+" in number:
                    idx += int(number[1:])
                else:
                    idx -= int(number[1:])
            elif instruction == "acc":
                if "+" in number:
                    acc += int(number[1:])
                elif "-" in number:
                    acc -= int(number[1:])
                idx += 1

    return (True, acc)


def adapt_instruction_and_run(lines):
    for instruction1, instruction2 in [("nop", "jmp"), ("jmp", "nop")]:
        for idx, line in enumerate(lines):
            if line.startswith(instruction1):
                adapted_lines = lines[:]
                adapted_lines[idx] = adapted_lines[idx].replace(
                    instruction1, instruction2
                )
                result = terminates_successfully_and_accumulates(adapted_lines)
                if result[0]:
                    return result[1]


def main():
    with open("8.txt") as input:
        lines = input.readlines()
    print(adapt_instruction_and_run(lines))

    return 0


if __name__ == "__main__":
    exit(main())
