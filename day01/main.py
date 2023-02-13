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

max_key = max(results, key=results.get)
print(f"{max_key} contains the highest amount with {results[max_key]}")