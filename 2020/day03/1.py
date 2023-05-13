def get_index(index, line):
    if index < len(line):
        return index
    return index % len(line)

tree_count = 0
x_index = 0

with open('input.txt') as input:
    data = [line.strip() for line in input.readlines()]
    del data[0]
    for line in data:
        x_index = get_index(x_index + 3, line)
        if line[x_index] == '#':
            tree_count += 1

print('part 1: ', tree_count)