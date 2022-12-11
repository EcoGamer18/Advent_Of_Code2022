def read_from_file_10():
    with open("inputs/input_day10.txt") as file:
        commands = []
        for line in file:
            command = []
            if line.strip():
                if len(line.strip().split(" ")) == 2:
                    command.append(line.strip().split(" ")[0])
                    command.append(int(line.strip().split(" ")[1]))
                else:
                    command.append(line.strip())
            commands.append(command)
    return commands


def solution_1(arr):
    result = 0
    cycles = []
    number_of_cycles = 0
    X = 1
    i = 0
    while i < len(arr) or cycles != []:
        # print(cycles, arr[i])
        number_of_cycles += 1
        if number_of_cycles in [20, 60, 100, 140, 180, 220]:
            # print(number_of_cycles, X)
            result += number_of_cycles * X
            if number_of_cycles == 220:
                break

        if len(cycles) == 0:
            if len(arr[i]) == 2:
                cycles.append([arr[i][1], 0])
            else:
                i += 1
        else:
            if cycles[0][1] == 0:
                X += cycles[0][0]
                cycles.pop(0)
                i += 1
    return result


def solution_2(arr):
    result = 0
    sprite = []
    line = []
    cycles = []
    number_of_cycles = 0
    X = 1
    i = 0
    while i < len(arr) or cycles != []:
        # print(cycles, arr[i])
        number_of_cycles += 1
        print(number_of_cycles)

        if len(line) == 40:
            sprite.append(line)
            line = []
        if number_of_cycles % 40 in [X, X + 1, X + 2]:
            line.append("#")
        else:
            line.append(".")

        if len(cycles) == 0:
            if len(arr[i]) == 2:
                cycles.append([arr[i][1], 0])
            else:
                i += 1
        else:
            if cycles[0][1] == 0:
                X += cycles[0][0]
                cycles.pop(0)
                i += 1

    if len(line) == 40:
        sprite.append(line)
    print("\n".join(["".join(x) for x in sprite]))
    return result


def print_day10():
    print(solution_1(read_from_file_10()))
    print(solution_2(read_from_file_10()))
