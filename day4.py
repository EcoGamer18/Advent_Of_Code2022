def read_from_file_4():
    with open("inputs/input_day4.txt") as file:
        tasks = []
        for line in file:
            elfs = []
            elf = []
            if line.strip():
                elf = line.strip().split(",")[0].split("-")
                elfs.append(elf)
                elf = line.strip().split(",")[1].split("-")
                elfs.append(elf)
            tasks.append(elfs)
    return tasks


def solution_1(arr):
    result = 0
    for x in arr:
        if (int(x[0][0]) <= int(x[1][0]) and int(x[0][1]) >= int(x[1][1])) or (
                int(x[1][0]) <= int(x[0][0]) and int(x[1][1]) >= int(x[0][1])):
            result += 1
    return result


def solution_2(arr):
    result = 0
    for x in arr:
        if (int(x[0][0]) in range(int(x[1][0]), int(x[1][1]) + 1) or int(x[0][1]) in range(int(x[1][0]),
                                                                                           int(x[1][1]) + 1)) or (
                int(x[1][0]) in range(int(x[0][0]), int(x[0][1]) + 1) or int(x[1][1]) in range(int(x[0][0]),
                                                                                               int(x[0][1]) + 1)):
            result += 1
    return result


def print_day4():
    print(solution_1(read_from_file_4()))
    print(solution_2(read_from_file_4()))
