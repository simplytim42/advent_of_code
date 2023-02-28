from rucksack import Rucksack
from pathlib import Path

sum_total = 0

with Path("./input.txt").open('r') as f:
    line = f.readline()
    while line:
        r = Rucksack(line.strip())
        sum_total = sum_total + r.getValueOfItem()
        line = f.readline()

print('part 1 sum total: ', sum_total)