'''
Created on Oct. 9, 2022

@author: Anmol Nagpal
'''

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        set_ = set(nums)
        max_ = self.getMax(set_)
        set_ = set_ - set([max_])
        max2 = self.getMax(set_)
        set_ = set_ - set([max2])
        max3 = self.getMax(set_)
        if max3 is not None:
            return max3
        else:
            return max_
            
    def getMax(self, set_):
        max_ = None
        for num in set_:
            if max_ is None:
                max_ = num
            else:
                max_ = max(num, max_)
        return max_