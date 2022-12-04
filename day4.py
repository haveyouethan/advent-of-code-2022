fp = 'aoc2022/day4.txt'

with open(fp,'r') as f:
    input = f.read().splitlines()

def is_subset(row):
    """
    Given a row of input, determine if either elf's ranges are a subset of either
    """
    
    # split input into a list of lists
    pair = row.split(',')
    elves = [x.split('-') for x in pair]    

    elf1_start, elf1_end = [int(x) for x in elves[0]]
    elf2_start, elf2_end = [int(x) for x in elves[1]]

    if (elf1_start >= elf2_start) and (elf1_end <= elf2_end):  # elf1 is a subset of elf2
        return True
    elif (elf2_start >= elf1_start) and (elf2_end <= elf1_end):  # elf2 is a subset of elf1
        return True
    else:
        return False

soln1 = sum([is_subset(x) for x in input])
print(f"Ans 1: {soln1}")


### PART TWO ###

def is_overlap(row):
    """
    Given a row of input, determine if either elf's ranges overlap each other
    """
    
    # split input into a list of lists
    pair = row.split(',')
    elves = [x.split('-') for x in pair]    

    elf1_start, elf1_end = [int(x) for x in elves[0]]
    elf2_start, elf2_end = [int(x) for x in elves[1]]

    # could potentially have abstracted the above transformation into another function for part 2
    # but nah

    if (elf2_start <= elf1_start <= elf2_end) \
        or (elf2_start <= elf1_end <= elf2_end) \
        or (elf1_start <= elf2_start <= elf1_end) \
        or (elf1_start <= elf2_end <= elf1_end):
        return True
    else:
        return False

soln2 = sum([is_overlap(x) for x in input])
print(f"Ans 2: {soln2}")
