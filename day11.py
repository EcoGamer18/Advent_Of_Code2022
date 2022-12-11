import re


class Monkey:
    def __init__(self, number, items, operation, test_divisible, test_true, test_false):
        self.items = items
        self.number = number
        self.operation = operation
        self.test_divisible = test_divisible
        self.test_true = test_true
        self.test_false = test_false
        self.number_of_items_tested = 0

    def __str__(self):
        return "Monkey number " + str(self.number) + \
               "\n\tItems: " + ", ".join(str(x) for x in self.items) + \
               "\n\tOperation: " + ", ".join(str(x) for x in self.operation) + \
               "\n\tTest divisible: " + str(self.test_divisible) + \
               "\n\tTest true: " + str(self.test_true) + \
               "\n\tTest false: " + str(self.test_false) + \
               "\n\tNumber of items tested: " + str(self.number_of_items_tested)


def read_from_file_11():
    monkeys = []
    with open("inputs/input_day11.txt") as file:
        for i, line in enumerate(file):
            if i % 7 == 0:
                monkey = Monkey(0, 0, 0, 0, 0, 0)
                p = re.compile(r"Monkey \d")
                result = p.findall(line)
                if result is not []:
                    monkey.number = int(result[0].split(" ")[1])

            if i % 7 == 1:
                items = []
                p = re.compile(r"Starting items:[ \d+,]*")
                result = p.findall(line)
                if result is not []:
                    result = result[0].split(":")[1].split(",")
                    items = [int(x) for x in result]
                monkey.items = items

            if i % 7 == 2:
                operation = []
                p = re.compile(r"Operation: new = old [+*] [\d]+")
                result = p.findall(line.strip())
                if len(result) != 0:
                    result[0] = result[0].split(" ")
                    operation.append(result[0][4])
                    operation.append(int(result[0][5]))
                else:
                    p = re.compile(r"Operation: new = old [+*] old")
                    result = p.findall(line.strip())
                    if result is not []:
                        result[0] = result[0].split(" ")
                        operation.append(result[0][4])
                        operation.append(result[0][5])
                monkey.operation = operation

            if i % 7 == 3:
                p = re.compile(r"Test: divisible by [\d]+")
                result = p.findall(line)
                if result is not []:
                    monkey.test_divisible = int(p.findall(line)[0].split(" ")[3])

            if i % 7 == 4:
                p = re.compile(r"If true: throw to monkey [\d]+")
                result = p.findall(line)
                if result is not []:
                    monkey.test_true = int(p.findall(line)[0].split(" ")[5])

            if i % 7 == 5:
                p = re.compile(r"If false: throw to monkey [\d]+")
                result = p.findall(line)
                if result is not []:
                    monkey.test_false = int(p.findall(line)[0].split(" ")[5])
                    monkeys.append(monkey)

    # print("\n".join([monkey.__str__() for monkey in monkeys]))
    return monkeys


def solution_1(monkeys):
    for i in range(20):
        aux_monkeys = monkeys
        for j in range(len(aux_monkeys)):
            x = aux_monkeys[j]
            x.number_of_items_tested += len(x.items)
            for p in range(len(x.items)):
                y = x.items[0]
                if x.operation[0] == "+":
                    if x.operation[1] == "old":
                        if ((y + y) // 3) % x.test_divisible == 0:
                            monkeys[x.test_true].items.append(((y + y) // 3))
                        else:
                            monkeys[x.test_false].items.append(((y + y) // 3))
                    else:
                        if ((y + x.operation[1]) // 3) % x.test_divisible == 0:
                            monkeys[x.test_true].items.append(((y + x.operation[1]) // 3))
                        else:
                            monkeys[x.test_false].items.append(((y + x.operation[1]) // 3))
                elif x.operation[0] == "*":
                    if x.operation[1] == "old":
                        if ((y * y) // 3) % x.test_divisible == 0:
                            monkeys[x.test_true].items.append(((y * y) // 3))
                        else:
                            monkeys[x.test_false].items.append(((y * y) // 3))
                    else:
                        if ((y * x.operation[1]) // 3) % x.test_divisible == 0:
                            monkeys[x.test_true].items.append(((y * x.operation[1]) // 3))
                        else:
                            monkeys[x.test_false].items.append(((y * x.operation[1]) // 3))
                x.items.pop(0)
        # print("\n".join(", ".join(str(k) for k in monkey.items) for monkey in monkeys))

    result = (sorted([x.number_of_items_tested for x in monkeys])[len(monkeys) - 1] *
              sorted([x.number_of_items_tested for x in monkeys])[len(monkeys) - 2])
    return result


def getDivs(N):
    factors = {1}
    maxP = int(N ** 0.5)
    p, inc = 2, 1
    while p <= maxP:
        while N % p == 0:
            factors.update([f * p for f in factors])
            N //= p
            maxP = int(N ** 0.5)
        p, inc = p + inc, 2
    if N > 1:
        factors.update([f * N for f in factors])
    return sorted(factors)


def solution_2(monkeys):
    test_divisibles = []
    for x in monkeys:
        test_divisibles.append(x.test_divisible)
    test_divisibles = list(set(test_divisibles))
    for x in monkeys:
        x.items = [list(y % z for z in test_divisibles) for y in x.items]
    for i in range(10000):
        aux_monkeys = monkeys
        for j in range(len(aux_monkeys)):
            x = aux_monkeys[j]
            x.number_of_items_tested += len(x.items)
            for p in range(len(x.items)):
                y = x.items[0]
                if x.operation[0] == "+":
                    if x.operation[1] == "old":
                        index = test_divisibles.index(x.test_divisible)
                        if (y[index] + y[index]) % x.test_divisible == 0:
                            monkeys[x.test_true].items.append([(y[z] + y[z]) % test_divisibles[z] for z in range(len(test_divisibles))])
                        else:
                            monkeys[x.test_false].items.append([(y[z] + y[z]) % test_divisibles[z] for z in range(len(test_divisibles))])
                    else:
                        index = test_divisibles.index(x.test_divisible)
                        if (y[index] + x.operation[1]) % x.test_divisible == 0:
                            monkeys[x.test_true].items.append([(y[z] + x.operation[1]) % test_divisibles[z] for z in range(len(test_divisibles))])
                        else:
                            monkeys[x.test_false].items.append([(y[z] + x.operation[1]) % test_divisibles[z] for z in range(len(test_divisibles))])
                elif x.operation[0] == "*":
                    if x.operation[1] == "old":
                        index = test_divisibles.index(x.test_divisible)
                        if (y[index] + y[index]) % x.test_divisible == 0:
                            monkeys[x.test_true].items.append([(y[z] * y[z]) % test_divisibles[z] for z in range(len(test_divisibles))])
                        else:
                            monkeys[x.test_false].items.append([(y[z] * y[z]) % test_divisibles[z] for z in range(len(test_divisibles))])
                    else:
                        index = test_divisibles.index(x.test_divisible)
                        if (y[index] * x.operation[1]) % x.test_divisible == 0:
                            monkeys[x.test_true].items.append([(y[z] * x.operation[1]) % test_divisibles[z] for z in range(len(test_divisibles))])
                        else:
                            monkeys[x.test_false].items.append([(y[z] * x.operation[1]) % test_divisibles[z] for z in range(len(test_divisibles))])
                x.items.pop(0)
        # print("\n".join(", ".join(str(k) for k in monkey.items) for monkey in monkeys))
    result = (sorted([x.number_of_items_tested for x in monkeys])[len(monkeys) - 1] *
              sorted([x.number_of_items_tested for x in monkeys])[len(monkeys) - 2])
    return result


def print_day11():
    print(solution_1(read_from_file_11()))
    print(solution_2(read_from_file_11()))
