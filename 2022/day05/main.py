from pathlib import Path
from copy import deepcopy

def interpret_instruction(instruction: str):
    move_start = instruction.find('move') + 5
    from_start = instruction.find('from') + 5
    to_start = instruction.find('to') + 3

    move_end = instruction.find(' ', move_start)
    from_end = instruction.find(' ', from_start)

    move_amount = int(instruction[move_start: move_end])
    from_container = int(instruction[from_start: from_end])
    to_container = int(instruction[to_start:])

    return move_amount, from_container, to_container

# part 1
# container data
containers_part1 = [
    ['Q','S','W','C','Z','V','F','T'],
    ['Q','R','B'],
    ['B','Z','T','Q','P','M','S'],
    ['D','V','F','R','Q','H'],
    ['J','G','L','D','B','S','T','P'],
    ['W','R','T','Z'],
    ['H','Q','M','N','S','F','R','J'],
    ['R','N','F','H','W'],
    ['J','Z','T','Q','P','R','B']
]
# prepare data for part2
containers_part2 = deepcopy(containers_part1)

# part 1
with Path('./instructions.txt').open() as file:
    instruction = file.readline()
    while instruction:
        amount_to_move, from_container, to_container = interpret_instruction(instruction)

        for i in range(1, amount_to_move + 1):
            crate = containers_part1[from_container - 1].pop()
            containers_part1[to_container - 1].append(crate)
        
        instruction = file.readline()

top_crates = []
for container in containers_part1:
    top_crates.append(container.pop())

print("part 1 answer: ", ''.join(top_crates))



#  part 2
with Path('./instructions.txt').open() as file:
    instruction = file.readline()
    while instruction:
        amount_to_move, from_container, to_container = interpret_instruction(instruction)

        crates = containers_part2[from_container - 1][- amount_to_move:]

        # update container to not contain the removed items
        containers_part2[from_container - 1] = containers_part2[from_container - 1][: - amount_to_move]

        containers_part2[to_container - 1].extend(crates)

        instruction = file.readline()


top_crates = []
for container in containers_part2:
    top_crates.append(container.pop())

print("part 2 answer: ", ''.join(top_crates))