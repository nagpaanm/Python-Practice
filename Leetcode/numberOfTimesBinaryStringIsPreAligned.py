'''
Created on Feb. 18, 2022

@author: nagpa
'''

class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        total = 0;
        maxFound = 0;
        found = 0;
        for num in flips:
            found += 1;
            maxFound = max(maxFound, num)
            if maxFound == found:
                total += 1
        return total