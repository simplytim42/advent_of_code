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

# with open('./input.txt') as file:
#     list_of_fish = [int(fish) for fish in file.readline().strip().split(',')]
#     for i in range(80):
#         list_of_fish = add_a_day(list_of_fish)
#     print('part1: ', len(list_of_fish))


with open('./input.txt') as file:
    list_of_fish = [int(fish) for fish in file.readline().strip().split(',')]
    tally = {}
    for fish in list_of_fish:
        if fish not in tally:
            tally[fish] = 1
        else:
            tally[fish] += 1

    total_fish_by_age = {}
    for day in range(256):
        temp_tally = {}
        for age, count in tally.items():
            if age == 0:
                if 6 not in temp_tally:
                    temp_tally.update({6:0})
                age_6_count = temp_tally[6]
                temp_tally.update({6:age_6_count + count})

                if 8 not in temp_tally:
                    temp_tally.update({8:0})
                age_8_count = temp_tally[8]
                temp_tally.update({8:age_8_count + count})
            else:
                if age-1 not in temp_tally:
                    temp_tally.update({age-1:0})

                age_count = temp_tally[age-1]
                temp_tally.update({age-1:age_count + count})
        tally = temp_tally
print("part 2:",sum(tally.values()))