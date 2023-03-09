with open("input.txt") as file:
    binary_numbers = [num.strip() for num in file.readlines()]

character_columns = [[] for i in range(len(binary_numbers[0]))]
for number in binary_numbers:
    for i in range(len(number)):
        character_columns[i].append(number[i])

gamma_rate = ""
epsilon_rate = ""
for column in character_columns:
    if column.count('1') > len(column) / 2:
        gamma_rate += "1"
        epsilon_rate += "0"
    else:
        gamma_rate += "0"
        epsilon_rate += "1"

gamma_rate = int(gamma_rate, 2)
epsilon_rate = int(epsilon_rate, 2)
power_consumption = gamma_rate * epsilon_rate
print("part 1: ", power_consumption)