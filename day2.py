def solution_1(arr):
    score = 0

    for x in arr:
        # rock
        if x[1] == 'X':
            # rock
            if x[0] == 'A':
                score += 3 + 1
            # paper
            if x[0] == 'B':
                score += 0 + 1
            # scissors
            if x[0] == 'C':
                score += 6 + 1
        # paper
        if x[1] == 'Y':
            # rock
            if x[0] == 'A':
                score += 6 + 2
            # paper
            if x[0] == 'B':
                score += 3 + 2
            # scissors
            if x[0] == 'C':
                score += 0 + 2
        # scissors
        if x[1] == 'Z':
            # rock
            if x[0] == 'A':
                score += 0 + 3
            # paper
            if x[0] == 'B':
                score += 6 + 3
            # scissors
            if x[0] == 'C':
                score += 3 + 3
    return score


def solution_2(arr):
    score = 0

    for x in arr:
        # lose
        if x[1] == 'X':
            # rock
            if x[0] == 'A':
                score += 0 + 3
            # paper
            if x[0] == 'B':
                score += 0 + 1
            # scissors
            if x[0] == 'C':
                score += 0 + 2
        # draw
        if x[1] == 'Y':
            # rock
            if x[0] == 'A':
                score += 3 + 1
            # paper
            if x[0] == 'B':
                score += 3 + 2
            # scissors
            if x[0] == 'C':
                score += 3 + 3
        # win
        if x[1] == 'Z':
            # rock
            if x[0] == 'A':
                score += 6 + 2
            # paper
            if x[0] == 'B':
                score += 6 + 3
            # scissors
            if x[0] == 'C':
                score += 6 + 1
    return score


def read_from_file_day2():
    with open("input_day2.txt") as file:
        values = []

        for line in file:
            value = []
            for x in line.split(" "):
                value.append(x[0])
            values.append(value)

    return values


def print_day2():
    print(solution_1(read_from_file_day2()))
    print(solution_2(read_from_file_day2()))
