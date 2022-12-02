fp = 'aoc2022/day2.txt'

with open(fp,'r') as f:
    input = f.read().splitlines()

# dictionaries to lookup scores for selected shapes and outcomes

# X: Rock, Y: Paper, Z: Scissors
score_shape = { 
    'X': 1,
    'Y': 2,
    'Z': 3
}

score_outcome = {
    'win': 6,
    'draw': 3,
    'lose': 0
}

# A/X: Rock, B/Y: Paper, C/Z: Scissors
outcome = {
    'A X': 'draw',
    'A Y': 'win',
    'A Z': 'lose',
    'B X': 'lose',
    'B Y': 'draw',
    'B Z': 'win',
    'C X': 'win',
    'C Y': 'lose',
    'C Z': 'draw'
}

# sum up scores of each round
score = 0
for round in input:
    score += (score_outcome[outcome[round]]  # score of outcome
              + score_shape[round[-1]])       # score of selected shape

soln1 = score
print(f"Ans 1: {soln1}")


### PART TWO ###

# X: lose, Y: draw, Z: win
outcome_mapping = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win'
}



outcome_shape = {
    'A X': 'Z',
    'A Y': 'X',
    'A Z': 'Y',
    'B X': 'X',
    'B Y': 'Y',
    'B Z': 'Z',
    'C X': 'Y',
    'C Y': 'Z',
    'C Z': 'X'
}

score = 0
for round in input:
    score += (score_outcome[outcome_mapping[round[-1]]]  # score of outcome
              + score_shape[outcome_shape[round]])  # score of selected shape

soln2 = score
print(f"Ans 2: {soln2}")

