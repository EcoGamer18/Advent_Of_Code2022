def read_from_file_1():
    with open("inputs/input_day1.txt") as file:
        elfs = []
        elf = []
        for line in file:
            if line.strip():
                elf.append(int(line.rstrip()))
            else:
                elfs.append(elf)
                elf = []
    return elfs


def solution_1(arr):
    return max(list(map(lambda x: sum(x), arr)))


def solution_2(arr):
    return sum(sorted(list(map(lambda x: sum(x), arr)), reverse=True)[:3])


def print_day1():
    print(solution_1(read_from_file_1()))
    print(solution_2(read_from_file_1()))
