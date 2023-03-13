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
total_cards = len(bingocards)
cards_which_have_won = 0
for number in numbers_called:

    for card in bingocards:
        if card.is_complete: continue
        card.mark_number(number)
        if card.has_won():
            cards_which_have_won += 1
            if cards_which_have_won == total_cards:
                print("part 2: ", int(number) * card.sum_of_remaining_numbers())
