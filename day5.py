fp = 'aoc2022/day5.txt'

with open(fp,'r') as f:
    input = f.read().splitlines()


# Split input into initial stack and commands
input_stacks = []
input_commands = []

for row in input:
    if row == '':
        continue
    elif row[0] == '[':
        input_stacks.append(row[1::4])
    elif row[:4] == 'move':
        input_commands.append(row)
    
#print(len(input_stacks), len(input_commands))


# Build stack using list of lists
max_stack_height = len(input_stacks)
num_stacks = len(input_stacks[0])

stacks = []

for i in range(num_stacks):
    stack = []
    for j in range(max_stack_height):
        ele = input_stacks[::-1][j][i]  # flip the stack, and build each stack from bottoms up
        if ele != ' ':
            stack.append(ele)
    stacks.append(stack)

# Transform command set
commands = []
for row in input_commands:
    commands.append([int(x) for x in row.split(' ')[1::2]])  # format of commands: [crates, origin, destination]


# Execute Order 66
for command in commands:
    crates, origin, dest = command
    for i in range(crates):
        crate = stacks[origin-1].pop()
        stacks[dest-1].append(crate)

soln1 = ''.join([x[-1] for x in stacks])
print(f"Ans 1: {soln1}")


### PART TWO ###



#print(f"Ans 2: {soln2}")
