'''
Created on Aug. 4, 2022

@author: Anmol Nagpal
'''

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        total = 0
        # O(n)
        for i in range(len(s) - 2):
            set_ = {s[i], s[i + 1], s[i + 2]}
            if len(set_) == 3:
                total += 1
        return total