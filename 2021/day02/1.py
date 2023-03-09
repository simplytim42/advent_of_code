with open("input.txt") as file:
    instructions = [instruction.strip() for instruction in file.readlines()]
    horizontal = 0
    depth = 0

    for instruction in instructions:
        direction, value = instruction.split(" ")
        value = int(value)

        if direction == "forward":
            horizontal += value
        elif direction == "up":
            depth -= value
        elif direction == "down":
            depth += value

print("part 1: ", horizontal * depth)