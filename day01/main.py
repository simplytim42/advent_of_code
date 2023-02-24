# challenge taken from https://adventofcode.com/2022/day/1

from pathlib import Path

file = Path("./data.txt")
results = {}

with file.open() as f:
    line = f.readline()
    index = 1
    while line:
        if line == '\n':
            index = index+1
            line = f.readline()
            continue

        key = "person" + str(index)
        line = int(line.strip())

        if key in results:
            results[key] = results[key] + line
        else:
            results[key] = line

        line = f.readline()

first_key = max(results, key=results.get)
print("Answer to Part 1:")
print(f"{first_key} contains the highest amount with {results[first_key]}")
print("\n")
print("Answer to Part 2:")

total_sum = results[first_key]
results[first_key] = 0
second_key = max(results, key=results.get)
total_sum = total_sum + results[second_key]

results[second_key] = 0
third_key = max(results, key=results.get)
total_sum = total_sum + results[third_key]
print(f"top three total is {total_sum}")