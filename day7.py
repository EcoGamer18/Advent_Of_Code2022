def read_from_file_7():
    with open("input_day7.txt") as file:
        commands = []
        for line in file:
            commands.append(line.strip())
    return commands


# solution if the names of the directories are all different
#
# def sum_values_of_directories(dir_content, dir_tree):
#     queue = []
#     for x, y in dir_tree.items():
#         if not y:
#             queue.append(x)
#     while queue:
#         queue_aux = []
#         print(queue)
#         for x in queue:
#             for y, z in dir_tree.items():
#                 if x in z and y != "/":
#                     queue_aux.append(y)
#                     dir_content[y] += dir_content[x]
#         queue = queue_aux
#     for x in dir_tree['/']:
#         dir_content["/"] += dir_content[x]
#
#
# def solution_1(arr):
#     current_dir = "/"
#     dir_content = {"/": []}
#     dir_dads = {"/": ""}
#     dir_tree = {"/": []}
#     index = 0
#     while index < len(arr):
#         if arr[index][:4] == '$ cd':
#             if arr[index][5:] != "..":
#                 dir_dads[arr[index][5:]] = current_dir
#                 dir_tree[current_dir].append(arr[index][5:])
#                 current_dir = arr[index][5:]
#                 dir_tree[current_dir] = []
#             else:
#                 current_dir = dir_dads[current_dir]
#         if arr[index][:4] == '$ ls':
#             index += 1
#             while index < len(arr) and arr[index][0] != "$":
#                 info = arr[index].split(" ")
#                 if info[0] == "dir":
#                     dir_content[info[1]] = []
#                     dir_tree[current_dir].append(info[1])
#                 else:
#                     dir_content[current_dir].append([int(info[0]), info[1]])
#                 index += 1
#             index -= 1
#         index += 1
#
#     for x, y in dir_content.items():
#         dir_content[x] = sum(z[0] for z in y)
#
#     for x, y in dir_tree.items():
#         dir_tree[x] = list(set(y))
#
#     sum_values_of_directories(dir_content, dir_tree)
#
#     sumF = 0
#     for item, value in dir_content.items():
#         if value <= 100000:
#             sumF += value
#
#     return sumF

class Node:
    # https://github.com/Fransandi/Advent-of-Code-Solutions/blob/main/2022/solutions/day7.py
    # object and solution inspired by this git
    # modified with an interpretation, not the best one
    # comments for learning
    def __init__(self, name, parent=None, size=0, is_dir=False):
        self.name = name
        self.parent = parent
        self.children = {}
        self.size = size
        self.is_dir = is_dir

    def add_child(self, child):
        self.children[child.name] = child
        self.size += child.size
        curr = self
        while curr.parent:
            curr.parent.size += child.size
            curr = curr.parent

    def __iter__(self):
        # https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/
        yield self
        for child in self.children.values():
            yield from child

    def __setitem__(self, name, filenode):
        self.children[name] = filenode

    def __getitem__(self, name):
        return self.children[name]

    def __contains__(self, name):
        return name in self.children

    def __hash__(self):
        return hash(str(self.name) + str(self.parent))

    def __str__(self):
        return self.name

    def __repr__(self):
        return (
            f"Node({self.name}, parent={self.parent},"
            f" size={self.size}, is_dir={self.is_dir})"
        )


def solution_1(arr):
    start = Node("/", None, 0, True)
    current_dir = start
    for x in arr:
        if x[0] == "$":
            if x[2:4] == "cd":
                if x[5:] == "/":
                    current_dir = start
                elif x[5:] == ".." and current_dir.parent:
                    current_dir = current_dir.parent
                elif x[5:] not in current_dir:
                    dir = Node(x[5:], current_dir, 0, True)
                    current_dir.add_child(dir)
                    current_dir = dir
                else:
                    current_dir = current_dir[x[5:]]
        elif x[:3] == "dir":
            dir = Node(x[4:], current_dir, 0, True)
            current_dir.add_child(dir)
        else:
            size, file = x.split(" ")
            file = Node(file, current_dir, int(size), False)
            current_dir.add_child(file)

    sum = 0
    for x in start:
        if x.is_dir and x.size <= 100000:
            sum += x.size

    return sum


def solution_2(arr):
    start = Node("/", None, 0, True)
    current_dir = start
    for x in arr:
        if x[0] == "$":
            if x[2:4] == "cd":
                if x[5:] == "/":
                    current_dir = start
                elif x[5:] == ".." and current_dir.parent:
                    current_dir = current_dir.parent
                elif x[5:] not in current_dir:
                    dir = Node(x[5:], current_dir, 0, True)
                    current_dir.add_child(dir)
                    current_dir = dir
                else:
                    current_dir = current_dir[x[5:]]
        elif x[:3] == "dir":
            dir = Node(x[4:], current_dir, 0, True)
            current_dir.add_child(dir)
        else:
            size, file = x.split(" ")
            file = Node(file, current_dir, int(size), False)
            current_dir.add_child(file)

    max_for_files = 70000000 - 30000000

    aux = start
    for x in start:
        if x.is_dir and start.size - max_for_files < x.size < aux.size:
            aux = x

    return aux.size


def print_day7():
    print(solution_1(read_from_file_7()))
    print(solution_2(read_from_file_7()))
