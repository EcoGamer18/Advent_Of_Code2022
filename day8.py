def read_from_file_8():
    with open("input_day8.txt") as file:
        tasks = []
        for line in file:
            elf = []
            if line.strip():
                elf = list(line.strip())
            tasks.append(elf)
    return tasks


def visible_right(arr, i, j):
    for x in range(j + 1, len(arr[i])):
        if arr[i][x] > arr[i][j] or (arr[i][x] >= arr[i][j] and x != j):
            return False
    return True


def visible_left(arr, i, j):
    for x in range(0, j):
        if arr[i][x] > arr[i][j] or (arr[i][x] >= arr[i][j] and x != j):
            return False
    return True


def visible_up(arr, i, j):
    for x in range(0, i):
        if arr[x][j] > arr[i][j] or (arr[x][j] >= arr[i][j] and x != i):
            return False
    return True


def visible_down(arr, i, j):
    for x in range(i + 1, len(arr)):
        if arr[x][j] > arr[i][j] or (arr[x][j] >= arr[i][j] and x != i):
            return False
    return True


def solution_1(arr):
    result = 0
    for i in range(1, len(arr) - 1):
        for j in range(1, len(arr[i]) - 1):
            if visible_down(arr, i, j) or visible_up(arr, i, j) \
                    or visible_left(arr, i, j) or visible_right(arr, i, j):
                result += 1
    return result + len(arr) * 2 + len(arr[0]) * 2 - 4


def score_visible_right(arr, i, j):
    score = 0
    for x in range(j + 1, len(arr[i])):
        score += 1
        if arr[i][x] > arr[i][j] or (arr[i][x] >= arr[i][j] and x != j):
            return score
    return score


def score_visible_left(arr, i, j):
    score = 0
    for x in reversed(range(0, j)):
        score += 1
        if arr[i][x] > arr[i][j] or (arr[i][x] >= arr[i][j] and x != j):
            return score
    return score


def score_visible_up(arr, i, j):
    score = 0
    for x in reversed(range(0, i)):
        score += 1
        if arr[x][j] > arr[i][j] or (arr[x][j] >= arr[i][j] and x != i):
            return score
    return score


def score_visible_down(arr, i, j):
    score = 0
    for x in range(i + 1, len(arr)):
        score += 1
        if arr[x][j] > arr[i][j] or (arr[x][j] >= arr[i][j] and x != i):
            return score
    return score


def solution_2(arr):
    result = 0
    for i in range(1, len(arr) - 1):
        for j in range(1, len(arr[i]) - 1):
            aux = score_visible_down(arr, i, j) * score_visible_up(arr, i, j) * score_visible_left(arr, i, j) \
                  * score_visible_right(arr, i, j)
            if result < aux:
                result = aux
    return result


def print_day8():
    print(solution_1(read_from_file_8()))
    print(solution_2(read_from_file_8()))
