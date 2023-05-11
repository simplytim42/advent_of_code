def separate_data(line):
    data = line.strip()
    rule, character, password = tuple(data.split(" "))
    return rule, character[:-1], password


def is_valid(rule, character, password):
    min, max = tuple(rule.split("-"))
    count = password.count(character)
    if count >= int(min) and count <= int(max):
        return True
    return False


with open("input.txt") as input:
    amount_valid = 0
    line = input.readline()
    while line:
        rule, character, password = separate_data(line)
        if is_valid(rule, character, password):
            amount_valid += 1
        line = input.readline()

print("part 1: ", amount_valid)
