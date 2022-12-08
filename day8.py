fp = 'aoc2022/day8.txt'
fp = 'aoc2022/day8_testcase.txt'

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


trees = trees()
#print(trees.grid[1][1:-1])
soln1 = trees.count_visible()
print(f"Ans 1: {soln1}") 


### PART TWO ###

# TODO
