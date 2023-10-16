'''
Created on Jul. 28, 2022

@author: Anmol Nagpal
'''

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        total = 0
        balanced = 0
        # O(n)
        for i in range(len(s)):
            if s[i] == "R":
                balanced += 1
            if s[i] == "L":
                balanced -= 1
            if balanced == 0:
                total +=1
        return total