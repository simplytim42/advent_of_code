from bingo import BingoCard

file = open("./input.txt")
numbers_called = [number for number in file.readline().split(",")]
bingocards = []

for line in file.readlines():
    # each card is preceded by a new line
    if line == "\n":
        if 'card' in locals():
            bingocards.append(card)
        card = BingoCard()
        continue

    card.add_row(line)

# start "playing" bingo and marking off numbers
bingo = False
for number in numbers_called:
    if bingo: break

    for card in bingocards:
        card.mark_number(number)
        if card.has_won():
            sum = card.sum_of_remaining_numbers()
            print("part 1: ", sum * int(number))
            bingo = True




