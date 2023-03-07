from pathlib import Path

class PairOfWorkers:
    def __init__(self, range1: list, range2: list) -> None:
        self.range1 = list(range(int(range1[0]), int(range1[1]) + 1))
        self.range2 = list(range(int(range2[0]), int(range2[1]) + 1))
    
    def rangesOverlapEntirely(self) -> bool:
        check1 = all(item in self.range1 for item in self.range2)
        check2 = all(item in self.range2 for item in self.range1)
        return check1 or check2

    def rangesOverlap(self) -> bool:
        set1 = set(self.range1)
        set2 = set(self.range2)
        overlap = set1.intersection(set2)
        return overlap


with Path("./input.txt").open() as file:
    line = file.readline()
    overlapEntirelyCount = 0
    overlapCount = 0
    while line:
        ranges = line.split(",")
        workers = PairOfWorkers(ranges[0].split('-'), ranges[1].split('-'))

        if workers.rangesOverlapEntirely():
            overlapEntirelyCount = overlapEntirelyCount + 1
        
        if workers.rangesOverlap():
            overlapCount = overlapCount + 1

        line = file.readline()

print("number of pairs with full overlap: ", overlapEntirelyCount)
print("number of pairs with any overlap at all: ", overlapCount)