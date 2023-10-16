'''
Created on Apr. 26, 2022

@author: Anmol Nagpal
'''

class Solution:
    def minimumMoves(self, s: str) -> int:
        index = 0
        count = 0
        # O(n)
        while index < len(s):
            if(s[index] == "X"):
                count += 1
                index += 3
            else:
                index += 1
        return count