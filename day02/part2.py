from pathlib import Path

class Rock:
    value = 1

class Paper:
    value = 2

class Scissors:
    value = 3

# Scores
LOSS = 0
DRAW = 3
WIN = 6

def generate_match_objects(raw_data):
    opponent_letter = raw_data[0].strip().lower()
    you_letter = raw_data[1].strip().lower()
    
    match opponent_letter:
        case 'a':
            opponent = Rock()
        case 'b':
            opponent = Paper()
        case 'c':
            opponent = Scissors()

    match you_letter:
        case 'x':
            outcome = LOSS
        case 'y':
            outcome = DRAW
        case 'z':
            outcome = WIN

    return outcome, opponent


def calculate_my_value(outcome, opponent):
    opponent_name = opponent.__class__.__name__

    if outcome == DRAW:
        return opponent.value

    if outcome == WIN and opponent_name == 'Rock':
        return Paper.value

    if outcome == WIN and opponent_name == 'Scissors':
        return Rock.value

    if outcome == WIN and opponent_name == 'Paper':
        return Scissors.value

    if outcome == LOSS and opponent_name == 'Scissors':
        return Paper.value

    if outcome == LOSS and opponent_name == 'Paper':
        return Rock.value
    
    if outcome == LOSS and opponent_name == 'Rock':
        return Scissors.value


# calculate score
total_score = 0
with Path('./puzzleinput.txt').open() as f:
    raw_data = f.readline()
    while raw_data:
        raw_data_list = raw_data.split(" ")
        outcome, opponent = generate_match_objects(raw_data_list)
        round_score = calculate_my_value(outcome, opponent)
        total_score = total_score + round_score + outcome
        raw_data = f.readline()

print("part 2 score: ", total_score)