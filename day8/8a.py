def exec_instructions(lines):
    lines_run_by_idx = []
    acc = 0
    idx = 0

    while -1 < idx < len(lines):
        if idx in lines_run_by_idx:
            return acc
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
                elif "-" in number:
                    idx -= int(number[1:])
            elif instruction == "acc":
                idx += 1
                if "+" in number:
                    acc += int(number[1:])
                elif "-" in number:
                    acc -= int(number[1:])


def main():
    with open("8.txt") as input:
        lines = input.readlines()
    print(exec_instructions(lines))
    return 0


if __name__ == "__main__":
    exit(main())