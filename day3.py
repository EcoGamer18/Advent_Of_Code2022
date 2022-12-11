from collections import Counter


def read_from_file_3():
    with open("inputs/input_day3.txt") as file:
        rucksacks = []
        for line in file:
            aux = line.rstrip()
            rucksack = [aux[:(int(len(aux)) // 2)], aux[(int(len(aux)) // 2):]]
            rucksacks.append(rucksack)

    return rucksacks


def common(str1, str2):
    # convert both strings into counter dictionary
    dict1 = Counter(str1)
    dict2 = Counter(str2)

    # take intersection of these dictionaries
    commonDict = dict1 & dict2

    if len(commonDict) == 0:
        print(-1)
        return

    # get a list of common elements
    commonChars = list(commonDict.elements())

    # sort list in ascending order to print resultant
    # string on alphabetical order
    commonChars = sorted(commonChars)

    # join characters without space to produce
    # resultant string
    return ''.join(set(commonChars))


def get_value(character):
    if 'a' <= character <= 'z':
        return 1 + ord(character) - ord('a')
    if 'A' <= character <= 'Z':
        return 27 + ord(character) - ord('A')


def solution_1(arr):
    result = 0

    for x in arr:
        commons = common(x[0], x[1])
        if commons != '':
            for y in commons:
                result += get_value(y)

    return result


def solution_2(arr):
    result = 0
    for i in range(len(arr)):
        arr[i] = ''.join(arr[i])

    for i in range(0, len(arr), 3):
        commons = common(arr[i], arr[i + 1])
        commons = common(commons, arr[i + 2])
        result += get_value(commons[0])

    return result


def print_day3():
    print(solution_1(read_from_file_3()))
    print(solution_2(read_from_file_3()))
