'''
Created on Jul. 6, 2022

@author: Anmol Nagpal
'''

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        mapping = {}
        # O(n)
        for num in nums:
            if num in mapping:
                mapping[num] += 1
            else:
                mapping[num] = 1
        # O(n)
        return sum([num for num in mapping.keys() if mapping[num] == 1])