fp = 'aoc2022/day9.txt'
#fp = 'aoc2022/day9_testcase.txt'

with open(fp,'r') as f:
    input = f.read().splitlines()


class tails():
    def __init__(self):
        self.cmds = [cmd.split(' ') for cmd in input]

        self.grid = self.init_grid()
        #self.tailed = self.init_grid(tailed=True)
        self.coords_head = self.init_coords()  # initial start point in grid
        self.coords_tail = self.init_coords()  # initial start point in grid
        self.coords_head_prev = self.coords_head  # trailing coords of head. used to update tail pos

    def dim_sum(self):
        """
        returns desired dimensions of grid based on set of commands 
        """
        x,x_min,x_max = 0,0,0
        y,y_min,y_max = 0,0,0
        for dir,val in self.cmds:
            val = int(val)
            if dir == 'U':
                y += val
                y_max = max(y_max,y)
            elif dir == 'D':
                y -= val
                y_min = min(y_min,y)
            elif dir == 'L':
                x -= val
                x_min = min(x_min,x)
            elif dir == 'R':
                x += val
                x_max = max(x_max,x)
        
        return x_min, x_max, y_min, y_max 


    def init_grid(self):
        x_min, x_max, y_min, y_max = self.dim_sum()
        width = x_max - x_min +1
        height = y_max - y_min +1

        return [[0]*height for x in range(width)]


    def init_coords(self):
        x_min, x_max, y_min, y_max = self.dim_sum()
        return [max(-x_min,0), max(-y_min,0)]


    def update_tail(self):
        """
        if head and tails are far apart, update tail to head's last known location
        """
        for i in range(2):
            if abs(self.coords_head[i] - self.coords_tail[i]) > 1:
                self.coords_tail = self.coords_head_prev  
                break
        x,y = self.coords_tail
        #print(x,y)
        self.grid[x][y] = 1


    def run_cmds(self):
        for dir,vals in self.cmds:
            vals = int(vals)
            print(dir,vals)
            tail_old = self.coords_tail
            if dir == 'U':
                for val in range(vals):
                    # hacky list comprehension to avoid pass-by-ref
                    # e.g. self.coords_head_prev = self.coords_head
                    self.coords_head_prev = [i for i in self.coords_head]  
                    self.coords_head[1] += 1
                    self.update_tail()
            elif dir == 'D':
                for val in range(vals):
                    self.coords_head_prev = [i for i in self.coords_head] 
                    self.coords_head[1] -= 1
                    self.update_tail()
            elif dir == 'L':
                for val in range(vals):
                    self.coords_head_prev = [i for i in self.coords_head] 
                    self.coords_head[0] -= 1
                    self.update_tail()
            elif dir == 'R':
                for val in range(vals):
                    self.coords_head_prev = [i for i in self.coords_head] 
                    self.coords_head[0] += 1
                    self.update_tail()
                    tail_new = self.coords_tail

                    #print(f'head: {self.coords_head_prev} > {self.coords_head}')
                    #print(f'tail: {tail_old} > {tail_new}')

    def count_visited(self):
        return sum([1 for x in self.grid for y in x if y is 1])


tails = tails()
tails.run_cmds()
soln1 = tails.count_visited()
print(f"Ans 1: {soln1}") 

