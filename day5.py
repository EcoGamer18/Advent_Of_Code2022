import re


def read_from_file_5():
    stacks = []
    with open("inputs/input_day5.txt") as file:
        crates = []
        move = []
        for line in file:
            p = re.compile(r"\[[ \w]*\]")
            result = p.findall(line)
            if result is not []:
                crates.append(list(map(lambda x: x[1], result)))
            p = re.compile(r"\d{1,3}")
            result = p.findall(line)
            if result is not []:
                move.append(p.findall(line))

    crates = [x for x in crates if x != []]
    moves = [x for x in move if x != []]

    number_of_stacks = len(moves[0])
    for i in range(number_of_stacks):
        stacks.append([])

    moves = moves[1:]

    for i in range(len(crates)):
        for j in range(len(crates[i])):
            if crates[i][j] != " ":
                stacks[j].append(crates[i][j])

    return stacks, moves


def solution_1(stacks, moves):
    for x in moves:
        number_of_moves = int(x[0])
        from_stack = int(x[1]) - 1
        to_stack = int(x[2]) - 1

        for i in range(number_of_moves):
            crate = stacks[from_stack].pop(0)
            if len(stacks[to_stack]) > 0:
                stacks[to_stack].insert(0, crate)
            else:
                stacks[to_stack].append(crate)

    result = []
    for y in stacks:
        if len(y) > 0:
            result.append(y[0])

    return "".join(result)


def solution_2(stacks, moves):
    for x in moves:
        number_of_moves = int(x[0])
        from_stack = int(x[1]) - 1
        to_stack = int(x[2]) - 1

        for i in range(number_of_moves):
            crate = stacks[from_stack].pop(0)
            if len(stacks[to_stack]) > 0:
                stacks[to_stack].insert(i, crate)
            else:
                stacks[to_stack].append(crate)

    result = []
    for y in stacks:
        if len(y) > 0:
            result.append(y[0])

    return "".join(result)


def print_day5():
    stacks, moves = read_from_file_5()
    print(solution_1(stacks, moves))
    stacks, moves = read_from_file_5()
    print(solution_2(stacks, moves))
