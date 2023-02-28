from rucksack import Rucksack, getValueOfItem, findGroupItem
from pathlib import Path

group_sum_total = 0

with Path("./input.txt").open('r') as f:
    line = f.readline()
    groupCounter = 1
    groupItems = []

    while line:
        rucksack = Rucksack(line.strip())

        groupItems.append(line.strip())

        groupCounter = groupCounter + 1
        if groupCounter > 3:
            groupCounter = 1
            groupItem = findGroupItem(groupItems)
            group_sum_total = group_sum_total + getValueOfItem(groupItem.pop())
            groupItems.clear()

        line = f.readline()

print('part 2 group sum total: ', group_sum_total)