def read_from_file_6():
    with open("inputs/input_day6.txt") as file:
        for line in file:
            tasks = line.strip()
    return tasks


def solution_1(arr):
    marker = arr[:4]
    for i in range(1, len(arr)):
        if len(set(marker)) == 4:
            return i + 3
        marker = arr[i:i + 4]
    return 0


def solution_2(arr):
    marker = arr[:14]
    for i in range(1, len(arr)):
        if len(set(marker)) == 14:
            return i + 13
        marker = arr[i:i + 14]
    return 0


def print_day6():
    print(solution_1(read_from_file_6()))
    print(solution_2(read_from_file_6()))
