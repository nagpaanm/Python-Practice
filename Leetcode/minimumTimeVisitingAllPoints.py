'''
Created on Mar. 18, 2022

@author: Anmol Nagpal
'''

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        hops = 0
        x1, y1 = points.pop()
        while points:
            x2,y2 = points.pop()
            hops += max(abs(y2-y1), abs(x2-x1))
            x1,y1 = x2, y2
        return hops