class Rucksack:
    itemInBoth = None

    def __init__(self, input: str):
        length = len(input)

        compartment1 = set(input[0:length//2])
        compartment2 = set(input[length//2:])

        self.itemInBoth = compartment1.intersection(compartment2)

    def getValueOfItem(self):
        letters = [
            'a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z',
            'A','B','C','D','E','F','G','H','I','J','K','L','M',
            'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        return letters.index(self.itemInBoth.pop()) + 1
