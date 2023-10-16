'''
Created on Nov. 30, 2022

@author: Anmol Nagpal
'''

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        ops = 0
        # O(n)
        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                amount = nums[i] - nums[i + 1] + 1
                nums[i + 1] += amount
                ops += amount
        return ops