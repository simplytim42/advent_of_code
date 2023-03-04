from pathlib import Path

class PacketMarkerFinder:
    def __init__(self) -> None:
        self.characters = []

    def addChar(self, char: str) -> None:
        if len(self.characters) > 3:
            self.characters.pop(0)
        self.characters.append(char)


    def isPacketMarker(self) -> bool:
        if len(self.characters) < 4:
            return False
        return True if len(set(self.characters)) == 4 else False


with Path('./datastream.txt').open() as file:
    data = file.readline()
    markerFinder = PacketMarkerFinder()
    count = 1
    for char in data:
        markerFinder.addChar(char)
        if markerFinder.isPacketMarker():
            print("part 1 answer: ", count)
            break
        count = count + 1
        