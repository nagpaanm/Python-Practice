'''
Created on Jul. 13, 2022

@author: Anmol Nagpal
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_ = set([])
        # O(n)
        for num in nums:
            if num in set_:
                return True
            set_.add(num)
        return False