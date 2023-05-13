def separate_data(line):
    data = line.strip()
    rule, character, password = tuple(data.split(" "))
    return rule, character[:-1], password


def is_valid(rule, character, password):
    first, second = tuple(rule.split("-"))
    first = int(first) - 1
    second = int(second) - 1
    first_condition = password[first] == character
    second_condition = password[second] == character

    if first_condition == second_condition:
        return False
    return True


with open("input.txt") as input:
    amount_valid = 0
    line = input.readline()
    while line:
        rule, character, password = separate_data(line)
        if is_valid(rule, character, password):
            amount_valid += 1
        line = input.readline()

print("part 2: ", amount_valid)
