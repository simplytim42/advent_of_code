from rucksack import Rucksack, getValueOfItem
from pathlib import Path

sum_total = 0

with Path("./input.txt").open('r') as f:
    line = f.readline()
    while line:
        rucksack = Rucksack(line.strip())
        sum_total = sum_total + getValueOfItem(rucksack.itemInBothCompartments.pop())
        line = f.readline()

print('part 1 sum total: ', sum_total)