'''
Created on Apr. 18, 2022

@author: Anmol Nagpal
'''

"""
An image is represented by an m x n integer grid image where image[i][j] 
represents the pixel value of the image.

You are also given three integers sr, sc, and newColor. You should perform a 
flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 
4-directionally to the starting pixel of the same color as the starting pixel, 
plus any pixels connected 4-directionally to those pixels (also with the same 
color), and so on. Replace the color of all of the aforementioned pixels with 
newColor.

Return the modified image after performing the flood fill.
"""

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        self.visited = []
        self.image = image
        # O(n)
        self.dfs(sr, sc, oldColor, newColor)
        return self.image
    
    def dfs(self, i, j, oldColor, newColor):
        if(self.image[i][j] != oldColor):
            return
        if self.image[i][j] == oldColor:
            self.image[i][j] = newColor
            self.visited.append((i,j))
        if(i > 0 and (i - 1, j) not in self.visited):
            self.dfs(i - 1, j, oldColor, newColor)
        if(i < len(self.image) - 1 and (i + 1, j) not in self.visited):
            self.dfs(i + 1, j, oldColor, newColor)
        if(j > 0 and (i, j - 1) not in self.visited):
            self.dfs(i, j - 1, oldColor, newColor)
        if(j < len(self.image[i]) - 1 and (i, j + 1) not in self.visited):
            self.dfs(i, j + 1, oldColor, newColor)