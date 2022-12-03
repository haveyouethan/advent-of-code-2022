fp = 'aoc2022/day3.txt'

with open(fp,'r') as f:
    input = f.read().splitlines()


def priority(c):
    """
    use ord() function to return priority of character 'c' 
    ord() returns the unicode code of characters, e.g.
    print(ord('A')) # 65
    print(ord('a')) # 97
    """
    if c.isupper():
        return ord(c)-64+26  # A through Z have priorities 27 through 52
    elif c.islower():
        return ord(c)-96  # a through z have priorities 1 through 26

def find_duplicate(rucksack):
    """
    find the duplicate item in both compartments of a rucksack
    """
    # // is int division, / is float division
    midpoint = len(rucksack)//2  # value used to partition the rucksacl 

    one = rucksack[:midpoint]
    two = rucksack[midpoint:]

    for c in one:
        if c in two:
            return c

# lazy solution
soln1 = sum([priority(x) for x in map(find_duplicate,input)])

# equivalent solution
soln1 = 0
for rucksack in input:
    dup = find_duplicate(rucksack)
    soln1 += priority(dup)

print(f"Ans 1: {soln1}")



### PART TWO ###

def badge_finder2000(group):
    """
    find common element (the badge) across all 3 rucksacks

    references on using set.intersections()
    + https://stackoverflow.com/questions/10066642/how-to-find-common-elements-in-list-of-lists
    + https://docs.python.org/3/library/stdtypes.html#frozenset.intersection
    """

    return set(group[0]).intersection(*group).pop()


soln2 = 0
for i in range(len(input)//3):
    group = input[3*i:3*i+3]  # partition inputs into groups of threes
    soln2 += priority(badge_finder2000(group))

    print(i, f"Ans 2: {soln2}")
