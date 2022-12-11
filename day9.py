def read_from_file_9():
    with open("input_day9.txt") as file:
        tasks = []
        for line in file:
            elf = []
            if line.strip():
                elf = [line.strip().split(" ")[0], int(line.strip().split(" ")[1])]
            tasks.append(elf)
    return tasks


def isInDirection(i_h, j_h, i_t, j_t):
    if i_h == i_t and j_t == j_h + 1:
        return "L"
    if i_h == i_t and j_t == j_h - 1:
        return "R"
    if i_h == i_t - 1 and j_t == j_h:
        return "U"
    if i_h == i_t + 1 and j_t == j_h:
        return "D"
    if i_h == i_t and j_t == j_h:
        return "start"
    return "diag"


def unique_coord(position):
    result = []
    for x in position:
        if x not in result:
            result.append(x)
    return result


def print_positions(positions):
    stop_i = max([x[0] for x in positions])
    stop_j = max([x[1] for x in positions])
    start_i = min([x[0] for x in positions])
    start_j = min([x[1] for x in positions])

    mapping = []
    print(start_i, stop_i)
    print(start_j, stop_j)
    for i in range(start_i, stop_i + 1):
        line = []
        for j in range(start_j, stop_j + 1):
            if [i, j] in positions:
                line.append("#")
            else:
                line.append(".")
        mapping.append(line)

    return "\n".join(["".join(x) for x in mapping])


def solution_1(arr):
    positions = []
    directions = {"U": [-1, 0], "D": [1, 0], "L": [0, -1], "R": [0, 1]}
    start_i_h = 1000
    start_j_h = 1000
    start_i_t = 1000
    start_j_t = 1000
    for x in arr:
        for index in range(x[1]):

            if isInDirection(start_i_h, start_j_h, start_i_t, start_j_t) == x[0]:
                start_i_t = start_i_t + directions[x[0]][0]
                start_j_t = start_j_t + directions[x[0]][1]
            elif isInDirection(start_i_h, start_j_h, start_i_t, start_j_t) == "diag" and isInDirection(
                    start_i_h + directions[x[0]][0], start_j_h + directions[x[0]][1], start_i_t, start_j_t) == "diag":
                start_i_t = start_i_h
                start_j_t = start_j_h

            start_i_h = start_i_h + directions[x[0]][0]
            start_j_h = start_j_h + directions[x[0]][1]

            positions.append([start_i_t, start_j_t])
            # print((print_positions(positions)))
    return len(unique_coord(positions))


def change_positions(x, start_i_h, start_j_h, start_i_t, start_j_t):
    directions = {"U": [-1, 0], "D": [1, 0], "L": [0, -1], "R": [0, 1]}
    if isInDirection(start_i_h, start_j_h, start_i_t, start_j_t) == x:
        start_i_t = start_i_t + directions[x][0]
        start_j_t = start_j_t + directions[x][1]
    elif isInDirection(start_i_h, start_j_h, start_i_t, start_j_t) == "diag" and isInDirection(
            start_i_h + directions[x][0], start_j_h + directions[x][1], start_i_t, start_j_t) == "diag":
        start_i_t = start_i_h
        start_j_t = start_j_h

    return start_i_t, start_j_t


def solution_2(arr):
    # not done
    directions = {"U": [-1, 0], "D": [1, 0], "L": [0, -1], "R": [0, 1]}
    i = [1000 for x in range(10)]
    j = [1000 for x in range(10)]
    positions = []
    for x in arr:
        for index in range(x[1]):
            for point in reversed(range(1, 10)):
                i[point], j[point] = change_positions(x[0], i[point - 1], j[point - 1],
                                                                                  i[point], j[point])
            i[0] = i[0] + directions[x[0]][0]
            j[0] = j[0] + directions[x[0]][1]
            positions.append([i[9], j[9]])
    print((print_positions(positions)))
    return len(unique_coord(positions))


def print_day9():
    print(solution_1(read_from_file_9()))
    print(solution_2(read_from_file_9()))
