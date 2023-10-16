'''
Created on Mar. 29, 2022

@author: Anmol Nagpal
'''

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        """
        total = 0
        for p in patterns:
            if p in word:
                total +=1
        """
        total = sum([1 for p in patterns if p in word])
        return total