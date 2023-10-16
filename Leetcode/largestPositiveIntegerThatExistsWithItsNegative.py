'''
Created on Dec. 7, 2022

@author: Anmol Nagpal
'''

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        # O(nlogn)
        nums.sort()
        if nums[0] > 0:
            return -1
        
        for i in range(len(nums)):
            if nums[i] < 0 and (nums[i] * -1) in nums:
                return nums[i] * -1
        return -1 