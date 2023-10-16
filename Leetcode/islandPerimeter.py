'''
Created on Nov. 5, 2022

@author: Anmol Nagpal
'''

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.total = 0
        self.visited = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    #self.dfs(i, j, grid)
                    self.total += self.surrounding(i, j, grid)
        return self.total

    def dfs(self, i, j, grid):
        if self.isValid(i, j, grid) and [i, j] not in self.visited:
            if grid[i][j] == 1:
                self.visited.append([i, j])
                self.total += self.surrounding(i, j, grid)
                self.dfs(i, j - 1, grid)
                self.dfs(i, j + 1, grid)
                self.dfs(i + 1, j, grid)
                self.dfs(i - 1, j, grid)

    def isValid(self, i, j, grid):
        if i > -1 and j > -1 and i < len(grid) and j < len(grid[0]):
            return True

    def surrounding(self, i, j, grid):
        total = 0
        if i == 0:
            total += 1
        if i == len(grid) - 1:
            total +=1 
        if j == 0:
            total += 1
        if j == len(grid[0]) - 1:
            total += 1
        if self.isValid(i, j - 1, grid) and [i, j] not in self.visited:
            if grid[i][j - 1] == 0:
                total += 1
        if self.isValid(i, j + 1, grid) and [i, j] not in self.visited:
            if grid[i][j + 1] == 0:
                total += 1
        if self.isValid(i + 1, j, grid) and [i, j] not in self.visited:
            if grid[i + 1][j] == 0:
                total += 1
        if self.isValid(i - 1, j, grid) and [i, j] not in self.visited:
            if grid[i - 1][j] == 0:
                total += 1
        return total