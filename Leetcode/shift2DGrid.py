'''
Created on Oct. 23, 2022

@author: Anmol Nagpal
'''

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        counter = 0
        size = len(grid[0])
        # O(n)
        dissemble = [num for lst in grid for num in lst]
        # O(k)
        while counter < k:
            dissemble = [dissemble[len(dissemble) - 1]] + dissemble[:-1]
            counter +=1
        grid = []
        row = []
        # O(n)
        for i in range(len(dissemble)):
            row.append(dissemble[i])
            if len(row) == size:
                grid.append(row)
                row = []
        return grid