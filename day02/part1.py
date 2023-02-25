from pathlib import Path

class Rock:
    value = 1

class Paper:
    value = 2

class Scissors:
    value = 3

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
            you = Rock()
        case 'y':
            you = Paper()
        case 'z':
            you = Scissors()

    return you, opponent

# Scores
LOSS = 0
DRAW = 3
WIN = 6

def calculate_round(you, opponent):
    you = you.__class__.__name__
    opponent = opponent.__class__.__name__

    if you == opponent:
        return DRAW

    if you == 'Paper' and opponent == 'Rock':
        return WIN

    if you == 'Paper' and opponent == 'Scissors':
        return LOSS

    if you == 'Rock' and opponent == 'Paper':
        return LOSS

    if you == 'Rock' and opponent == 'Scissors':
        return WIN

    if you == 'Scissors' and opponent == 'Paper':
        return WIN
    
    if you == 'Scissors' and opponent == 'Rock':
        return LOSS


# opponent
a = Rock()
b = Paper()
c = Scissors()

# you
x = Rock()
y = Paper()
z = Scissors()


# calculate score
total_score = 0
with Path('./puzzleinput.txt').open() as f:
    raw_data = f.readline()
    while raw_data:
        raw_data_list = raw_data.split(" ")
        you, opponent = generate_match_objects(raw_data_list)
        round_score = calculate_round(you, opponent)
        total_score = total_score + round_score + you.value
        raw_data = f.readline()

print("part 1 score: ", total_score)