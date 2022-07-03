'''
Created on Jul. 3, 2022

@author: Anmol Nagpal
'''

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = len(nums)
        # O(n)
        lst = [i for i in range(1, s + 1)]
        return set(lst) - set(nums)
        
        