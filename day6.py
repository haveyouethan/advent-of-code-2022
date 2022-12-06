fp = 'aoc2022/day6.txt'

with open(fp,'r') as f:
    input = f.read()

signal_length = len(input)

def is_marker(str, chars):
    return len(set(str)) == chars


for i in range(4,signal_length):
    four_char = input[i-4:i]
    if is_marker(four_char, 4):
        soln1 = i
        break

print(f"Ans 1: {soln1}")


### PART TWO ###

for i in range(14,signal_length):
    four_char = input[i-14:i]
    if is_marker(four_char, 14):
        soln2 = i
        break

print(f"Ans 2: {soln2}")
