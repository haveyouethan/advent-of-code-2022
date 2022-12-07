fp = 'aoc2022/day7.txt'
#fp = 'aoc2022/day7_testcase.txt'

with open(fp,'r') as f:
    input = f.read().splitlines()


class Node:
    def __init__(self, name, parent):
        self.name = name
        self.size = 0  # sum of child directories and files
        self.parent = parent
    
    def __repr__(self):
        if self.parent:
            return (f'(size={str(self.size)}, parent={self.parent.name})')
        else: 
            return (f'(size={str(self.size)}, parent=None)')

    def update_size(self, size):
        self.size += size
        if self.parent is not None:  # updates all parent directories up to root folder
            self.parent.update_size(size)  
        # print(self.name, self.size)

# use a dict to store file system
fs = {}

# init root node for '/'
# dict will allow instant inspection of respective nodes
fs['/'] = Node('/', None)


# traverse input
for row in input:
    cmd = row.split(' ')
    if cmd[0] == '$':
        if cmd[1] == 'cd':
            dir_name = cmd[2]
            if dir_name == '/':  # init root folder
                curr_node = fs['/']

            elif dir_name == '..':  # up one level
                curr_node = curr_node.parent

            else:  # down to child node
                curr_node = fs[f'{curr_node.name}/{dir_name}']

               
        # Can ignore '$ ls' commands

    elif cmd[0] == 'dir':  # new child directory
        dir_name = f'{curr_node.name}/{cmd[1]}'
        fs[dir_name] = Node(dir_name, curr_node)

        
    else:  # is file
        file_size, file_name = cmd
        curr_node.update_size(int(file_size))


soln1 = sum([v.size for k,v in fs.items() if (v.size<=1E5)])
#print(fs)
print(f"Ans 1: {soln1}")  #1084134


### PART TWO ###
space_req = fs['/'].size - 4E7
soln2 = min([v.size for k,v in fs.items() if (v.size >= space_req)])

print(f"Ans 2: {soln2}")
