'''
Created on Sep. 28, 2022

@author: Anmol Nagpal
'''

class Solution:
    def countElements(self, nums: List[int]) -> int:
        max_ = max(nums)
        min_ = min(nums)
        count = 0
        for num in nums:
            if num < max_ and num > min_:
                count += 1
        return count