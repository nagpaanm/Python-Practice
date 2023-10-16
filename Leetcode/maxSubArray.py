'''
Created on Mar. 14, 2022

@author: Anmol Nagpal
'''
class Solution:
    
    #kadane's algo - O(n) time
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)