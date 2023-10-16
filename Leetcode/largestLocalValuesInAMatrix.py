'''
Created on Oct. 2, 2022

@author: Anmol Nagpal
'''

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        storage = [[0 for j in range(len(grid[i]) - 2)] for i in range(len(grid) - 2)]
        for i in range(len(storage)):
            for j in range(len(storage[i])):
                rows = grid[i][j:j + 3] + grid[i + 1][j:j + 3] + grid[i + 2][j:j + 3]
                storage[i][j] = max(rows)
        return storage