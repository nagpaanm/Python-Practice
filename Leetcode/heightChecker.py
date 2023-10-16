'''
Created on May 8, 2022

@author: Anmol Nagpal
'''

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_list = heights.copy()
        sorted_list.sort()
        count = 0
        for i in range(len(sorted_list)):
            if heights[i] != sorted_list[i]:
                count +=1
        return count