with open("input.txt") as file:
    instructions = [instruction.strip() for instruction in file.readlines()]
    horizontal = 0
    depth = 0
    aim = 0

    for instruction in instructions:
        direction, value = instruction.split(" ")
        value = int(value)

        if direction == "forward":
            horizontal += value
            depth += aim * value
        elif direction == "up":
            aim -= value
        elif direction == "down":
            aim += value

print("part 2: ", horizontal * depth)