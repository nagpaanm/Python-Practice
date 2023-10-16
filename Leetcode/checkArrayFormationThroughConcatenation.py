'''
Created on May 11, 2022

@author: Anmol Nagpal
'''

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        # O(n)
        mapping = {x[0]: x for x in pieces}
        res = []
        # O(n)
        for num in arr:
            if num in mapping:
                res += mapping[num]
            
        return res == arr