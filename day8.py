fp = 'aoc2022/day8.txt'
#fp = 'aoc2022/day8_testcase.txt'

with open(fp,'r') as f:
    input = f.read().splitlines()


class trees():
    def __init__(self):
        self.grid = input
        self.width = len(self.grid[0])
        self.height = len(self.grid)
    
    def __repr__(self):
        return f'dimensions: {self.width}W x {self.height}H'

    def is_visible(self, i,j):
        """
        Returns True if tree located at coords (i,j) is visible from any direction
        """
        # for the case of outer edges of the grid
        if (i == 0) or (i == self.height-1) or (j == 0) or (j == self.width-1):
            return True

        # check the NSEW visibility
        # Condition: value must be taller than all other trees in between
        elif self.grid[i][j] > max(self.grid[i][:j]):  # Eastward vis
            return True

        elif self.grid[i][j] > max(self.grid[i][j+1:]):  # Westward vis
            return True

        elif self.grid[i][j] > max([x[j] for x in self.grid[i+1:]]):  # Northward vis
            return True

        elif self.grid[i][j] > max([x[j] for x in self.grid[:i]]):  # Southward vis
            return True


    def count_visible(self):
        """
        Returns number of visible trees in tree grid
        Iterates through all members of the grid and counts visible trees
        """
        count = 0
        for i, row in enumerate(self.grid):
            for j, col in enumerate(row):
                if self.is_visible(i,j):
                    # print(i,j, self.grid[i][j])
                    count += 1
        return count


    ## PART TWO FUNCTIONS ##

    def scenic_score(self, i,j):
        """
        Returns Scenic Score of tree located at coords (i,j)
        """
        # for the case of outer edges of the grid
        if (i == 0) or (i == self.height-1) or (j == 0) or (j == self.width-1):
            return 0  # all trees at the edge have score 0
    

        # check the NSEW visibility, oriented from origin i,j

        view_n = [x[j] for x in self.grid[:i]][::-1]
        view_s = [x[j] for x in self.grid[i+1:]]
        view_e = [x for x in self.grid[i][j+1:]]
        view_w = [x for x in self.grid[i][:j]][::-1]

        views = [view_n, view_w, view_s, view_e]

        score = 1
        ht = self.grid[i][j] # current height

        for idx_view,view in enumerate(views):
            for idx,val in enumerate(view):
                if val >= ht:
                    print(1,idx+1)
                    break  # stops current view, multiples the score, and jumps to next loop/view 
            score *= (idx+1)  # this is the number of trees

        return score
    

    def max_scenic_score(self):
        return max([self.scenic_score(i,j) for i,row in enumerate(self.grid) for j, col in enumerate(row)])



trees = trees()

soln1 = trees.count_visible()
print(f"Ans 1: {soln1}") 


### PART TWO ###
soln2 = trees.max_scenic_score()
print(f"Ans 2: {soln2}") 
