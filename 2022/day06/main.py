from pathlib import Path

class UniqueCombinationFinder:
    def __init__(self, uniqueAmount: int) -> None:
        self.characters = []
        self.uniqueAmount = uniqueAmount

    def addChar(self, char: str) -> None:
        if len(self.characters) >= self.uniqueAmount:
            self.characters.pop(0)
        self.characters.append(char)

    def isPacketMarker(self) -> bool:
        if len(self.characters) < self.uniqueAmount:
            return False
        return True if len(set(self.characters)) == self.uniqueAmount else False

# part 1
with Path('./datastream.txt').open() as file:
    data = file.readline()
    packetMarkerFinder = UniqueCombinationFinder(4)
    count = 1
    for char in data:
        packetMarkerFinder.addChar(char)
        if packetMarkerFinder.isPacketMarker():
            print("part 1 answer: ", count)
            break
        count = count + 1

#  part 2
with Path('./datastream.txt').open() as file:
    data = file.readline()
    messageMarkerFinder = UniqueCombinationFinder(14)
    count = 1
    for char in data:
        messageMarkerFinder.addChar(char)
        if messageMarkerFinder.isPacketMarker():
            print("part 2 answer: ", count)
            break
        count = count + 1