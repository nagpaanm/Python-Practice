'''
Created on May 1, 2022

@author: Anmol Nagpal
'''

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        smallest = 10000
        index = None
        # runtime => O(n)
        # spacetime => O(1)
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                md = self.calculate_MD(x, y, points[i][0], points[i][1])
                if md < smallest:
                    smallest = md
                    index = i
        return index if index != None else -1
    
    def calculate_MD(self, x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)