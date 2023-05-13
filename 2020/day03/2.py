def get_index(index, line):
    if index < len(line):
        return index
    return index % len(line)

rules = [
    (1,1),
    (3,1),
    (5,1),
    (7,1),
    (1,2)
]

total_trees = []

for rule in rules:
    tree_count = 0
    x_index = 0
    right, down = rule

    with open('input.txt') as input:
        data = [line.strip() for line in input.readlines()]

        while data:
            if down != 0:
                del data[0]
                down -= 1
                continue
            _, down = rule

            x_index = get_index(x_index + right, data[0])
            if data[0][x_index] == '#':
                tree_count += 1

        total_trees.append(tree_count)

from math import prod
print('part 2: ', prod(total_trees))
