def add_a_day(list_of_fish: list):
    amount_to_append = 0
    for index, fish in enumerate(list_of_fish):
        if fish == 0:
            amount_to_append += 1
            list_of_fish[index] = 6
        else:
            list_of_fish[index] -= 1
    
    for i in range(amount_to_append):
        list_of_fish.append(8)

    return list_of_fish

with open('./input.txt') as file:
    list_of_fish = [int(fish) for fish in file.readline().split(',')]

    for i in range(80):
        list_of_fish = add_a_day(list_of_fish)
    
    print('part1: ', len(list_of_fish))
    