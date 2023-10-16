'''
Created on Feb. 21, 2022

@author: Anmol Nagpal
'''

"""
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' 
and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 
and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates 
to target.
"""

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.memo = {}
        return self.dp(target, 0, nums, len(nums) - 1)
    
    def dp(self, target, total, nums, index):
        if (index, total) in self.memo:
            return self.memo[(index, total)]
        if(index < 0):
            if(target == total):
                return 1
            return 0
        ways = self.dp(target, total + nums[index], nums, index - 1) + self.dp(target, total - nums[index], nums, index - 1)
        self.memo[(index, total)] = ways
        return ways